# Module 2: Database Interactions (File Handling Version)

import json
import os
from fallback import STATIC_CROPS

class DatabaseManager:
    def __init__(self, filename='crops.json'):
        self.filename = filename

    def get_all_crops(self):
        """Fetches crops from the JSON file. Uses static default data if file doesn't exist."""
        if not os.path.exists(self.filename):
            # If the file doesn't exist, return the static default data from fallback
            return STATIC_CROPS
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                if not data: # Handles empty file
                    return STATIC_CROPS
                return data
        except (json.JSONDecodeError, IOError):
            return STATIC_CROPS

    def add_new_crop(self, name, cost, yield_value, price):
        """Saves a new crop data to the existing JSON file."""
        # 1. Load existing data first
        current_data = self.get_all_crops()
        
        # 2. Then, Add new data
        current_data[name.lower()] = {
            "default_cost_per_acre": float(cost),
            "default_expected_yield": float(yield_value),
            "default_price": float(price)
        }
        
        # 3. Save back to file
        try:
            with open(self.filename, 'w') as f:
                json.dump(current_data, f, indent=4)
            return True, "Task Successful: Crop saved to 'crops.json' file."
        except IOError as e:
            return False, f"File Error: {e}"