import json
import re
import os
import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.myscheme.gov.in"
SCHEMES_LIST_URL = BASE_URL + "/search"

def setup_driver():
    chrome_options = Options()
    # Uncomment the next line for headless mode (no browser window)
    # chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1280, 1024)
    return driver

def parse_eligibility_rules(text: str) -> dict:
    rules = {}
    if not text:
        return rules
    text = text.lower()
    age_matches = re.findall(r'(\d+)\s*(to|-)\s*(\d+)\s*years', text)
    if age_matches:
        rules['min_age'] = int(age_matches[0][0])
        rules['max_age'] = int(age_matches[0][2])
    else:
        min_age = re.search(r'above\s*(\d+)\s*years|min.* (\d+)\s*years', text)
        if min_age:
            rules['min_age'] = int(min_age.group(1) or min_age.group(2) or 0)
        max_age = re.search(r'below\s*(\d+)\s*years|up to\s*(\d+)\s*years', text)
        if max_age:
            rules['max_age'] = int(max_age.group(1) or max_age.group(2) or 0)

    income_match = re.search(r'less than.*?₹\s*([\d,.]+)', text)
    if income_match:
        income_str = income_match.group(1).replace(',', '')
        try:
            rules['income_lakhs_max'] = float(income_str) / 100000
        except ValueError:
            pass

    occupations = []
    if 'student' in text:
        occupations.append('Student')
    if 'farmer' in text:
        occupations.append('Farmer')
    if 'business' in text or 'entrepreneur' in text:
        occupations.append('Business Owner')
    if occupations:
        rules['occupation'] = occupations

    if 'female' in text or 'women' in text or 'girl' in text:
        rules['gender'] = 'Female'
    elif 'male' in text:
        rules['gender'] = 'Male'

    return rules

def extract_schemes_from_listing(html):
    soup = BeautifulSoup(html, "lxml")
    scheme_cards = soup.find_all("div", class_="mx-auto rounded-xl shadow-md overflow-hidden w-full group hover:shadow-lg bg-white dark:bg-dark dark:shadow-xl dark:hover:shadow-2xl")
    if not scheme_cards:  # fallback for other list layouts
        scheme_cards = soup.find_all("div", class_="flex flex-col")
    schemes = []
    for card in scheme_cards:
        # --- Name and Link ---
        h2 = card.find("h2", id=lambda s: s and s.startswith("scheme-name"))
        name = None
        link = None
        if h2:
            a = h2.find('a', href=True)
            if a:
                name = a.get_text(strip=True)
                link = BASE_URL + a['href']
        # --- Ministry ---
        ministry = None
        min_h2 = card.find("h2", class_=lambda s: s and "font-normal" in s and "text-raven" in s)
        if min_h2:
            ministry = min_h2.get_text(strip=True)
        # --- Description ---
        desc = None
        desc_span = card.find("span", attrs={"aria-label": lambda x: x and "Brief description:" in x})
        if desc_span:
            desc = desc_span.get_text(strip=True)
        # --- Tags ---
        tag_divs = card.find_all("div", attrs={"aria-label": lambda x: x and "Filter by tag:" in x})
        tags = [d.get_text(strip=True) for d in tag_divs]
        if name and link:
            schemes.append({
                "scheme_name": name,
                "official_link": link,
                "ministry": ministry,
                "description": desc,
                "tags": tags,
            })
    return schemes

def extract_details_page(driver, url):
    try:
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        detail_soup = BeautifulSoup(driver.page_source, "lxml")
        benefits_div = detail_soup.find('h2', string=re.compile("Benefits", re.I))
        benefits = benefits_div.find_next_sibling('div').get_text(strip=True, separator='\n') if benefits_div and benefits_div.find_next_sibling('div') else 'N/A'
        eligibility_div = detail_soup.find('h2', string=re.compile("Eligibility", re.I))
        eligibility_text = eligibility_div.find_next_sibling('div').get_text(strip=True) if eligibility_div and eligibility_div.find_next_sibling('div') else ''
        documents_div = detail_soup.find('h2', string=re.compile("Documents Required", re.I))
        documents = []
        if documents_div and documents_div.find_next_sibling('div'):
            docs_list = documents_div.find_next_sibling('div').find_all('li')
            documents = [li.get_text(strip=True) for li in docs_list]
        return benefits, eligibility_text, documents
    except Exception as e:
        print(f"   [Error scraping details: {url}] {e}")
        return 'N/A', '', []

def scrape_schemes_automatic():
    driver = setup_driver()
    print("🚀 Selenium driver started.")
    try:
        driver.get(SCHEMES_LIST_URL)
        # Try cookie consent
        try:
            cookie_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept All')]"))
            )
            cookie_button.click()
            time.sleep(2)
        except Exception:
            pass

        # Wait for the first listing cards
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "scheme-card-wrapper")))
        # --- Automatic scrolling ---
        print("   Auto scrolling to load all schemes...")
        last_count = 0
        same_count_tries = 0
        MAX_TRIES = 10
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2.5)
            # use card wrapper as anchor
            scheme_cards = driver.find_elements(By.CLASS_NAME, 'scheme-card-wrapper')
            current_count = len(scheme_cards)
            if current_count == last_count:
                same_count_tries += 1
                if same_count_tries >= MAX_TRIES:
                    break
            else:
                same_count_tries = 0
            last_count = current_count
            print(f"   Loaded {last_count} scheme cards...")
        print(f"✅ All schemes loaded: {last_count}")
        # --- Parse summary info from loaded page ---
        schemes = extract_schemes_from_listing(driver.page_source)
        print(f"✅ Extracted {len(schemes)} from list, fetching details for each.")

        # --- Visit each detail page and add additional info ---
        final_schemes = []
        for idx, item in enumerate(schemes):
            print(f"   ({idx+1}/{len(schemes)}) {item['scheme_name']} ...", end='', flush=True)
            benefits, eligibility_text, documents = extract_details_page(driver, item['official_link'])
            final_schemes.append({
                "scheme_id": item['official_link'].split("/")[-1],
                "scheme_name": item['scheme_name'],
                "ministry": item['ministry'],
                "description": item['description'],
                "benefits": benefits,
                "tags": item['tags'],
                "eligibility_rules": parse_eligibility_rules(eligibility_text),
                "official_link": item['official_link'],
                "required_documents": documents
            })
            print("done.")
            time.sleep(0.5)  # Nice to servers.

        # Save to schemes.json in the same dir as script (or edit to your needs)
        outdir = os.path.join(os.path.dirname(__file__), '..')
        output_path = os.path.abspath(os.path.join(outdir, 'schemes.json'))
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(final_schemes, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Done! Saved {len(final_schemes)} schemes to {output_path}")

    finally:
        driver.quit()
        print("✅ Selenium driver closed.")

if __name__ == "__main__":
    scrape_schemes_automatic()
