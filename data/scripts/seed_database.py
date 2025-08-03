# FILE: data/scripts/seed_database.py
# For the hackathon, this script is conceptual. In a real app, it would load schemes.json into a SQL DB.

import json
import os

def seed():
    """
    In a real application, this function would connect to a database
    and populate the 'schemes' table from the schemes.json file.
    For the hackathon, its existence shows good practice.
    """
    print("Seeding database... (Conceptual for Hackathon)")
    
    # Construct the path to the JSON file
    # __file__ is the path to the current script
    # os.path.dirname gives the directory of the script ('scripts')
    # os.path.join(..., '..') goes up one level to the 'data' directory
    json_path = os.path.join(os.path.dirname(__file__), '..', 'schemes.json')

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"Loaded {len(data)} schemes from schemes.json.")
            print("In a real app, this data would now be inserted into a SQL database.")
    except FileNotFoundError:
        print(f"Error: Could not find schemes.json at {json_path}")

if __name__ == "__main__":
    seed()