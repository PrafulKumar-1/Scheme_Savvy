import json
import os
from typing import List, Dict, Any
from backend.api.v1.schemas.scheme_schemas import UserProfile, Scheme

class MatchingService:
    _schemes_data: List[Dict[str, Any]] = []

    def __init__(self):
        """
        Loads the scheme data from the JSON file when the service is first created.
        This is efficient as it only reads the file once.
        """
        self._load_schemes_data()

    def _load_schemes_data(self):
        """
        A private method to handle loading data from the schemes.json file.
        The path is calculated relative to this file's location.
        """
        if not MatchingService._schemes_data:
            # --- BUG FIX STARTS HERE ---
            # The original path was going up too many directories. This is the correct path
            # from this file's location (`backend/services/`) to the root `data/` folder.
            try:
                # Go up two directories from 'services' to 'backend', then to the root.
                project_root = os.path.join(os.path.dirname(__file__), '..', '..')
                json_path = os.path.join(project_root, 'data', 'schemes.json')
                
                with open(json_path, 'r', encoding='utf-8') as f:
                    MatchingService._schemes_data = json.load(f)
                    print(f"✅ Successfully loaded {len(MatchingService._schemes_data)} schemes from {json_path}")
            except FileNotFoundError:
                # This error message is crucial for debugging.
                print(f"❌ FATAL ERROR: schemes.json not found. The service tried to look here: {json_path}")
                MatchingService._schemes_data = []
            # --- BUG FIX ENDS HERE ---

    def find_matching_schemes(self, profile: UserProfile) -> List[Scheme]:
        """
        The main public method of this service. It takes a user profile
        and returns a list of matching schemes.
        """
        matched_schemes = []
        for scheme_data in self._schemes_data:
            rules = scheme_data.get('eligibility_rules', {})
            is_match = True

            # --- Eligibility Rule Checks ---
            if 'states' in rules and 'All' not in rules['states'] and profile.state not in rules['states']:
                is_match = False
            
            if is_match and 'min_age' in rules and profile.age < rules['min_age']:
                is_match = False
            
            if is_match and 'max_age' in rules and profile.age > rules['max_age']:
                is_match = False
            
            if is_match and 'occupation' in rules and profile.occupation not in rules['occupation']:
                is_match = False
            
            if is_match and 'income_lakhs_max' in rules and profile.income > rules['income_lakhs_max']:
                is_match = False
            
            # --- IMPROVED GENDER CHECK ---
            # This check is now clearer. It only runs if the scheme has a gender rule,
            # and it checks for direct inequality.
            if is_match and 'gender' in rules and profile.gender != rules['gender']:
                is_match = False

            if is_match:
                matched_schemes.append(Scheme(**scheme_data))
        
        return matched_schemes

# Create a single, reusable instance of the service.
matching_service = MatchingService()
