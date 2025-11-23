# Module 5: Entry Point & User Interface

import sys
import os
from database import DatabaseManager
from corelogic import ProfitCalculator

def main():
    # Initializes the database manager i.e creates or reads crops.json file
    db = DatabaseManager()
    
    while True:
        print("\n" + "="*40)
        print("   CROP PROFIT PREDICTION CALCULATOR   ")
        print("="*40)
        
        # We check if the JSON file exists to report status or create a new one
        if os.path.exists(db.filename):
            status = f"ONLINE (Stored in: {db.filename})"
        else:
            status = "INITIALIZING (Will create file on saving new crop)"
            
        print(f"System Status: {status}\n")

        print("1. Calculate Profit")
        print("2. Add New Crop Definition")
        print("3. Run System Tests")
        print("4. Exit")
        
        choice = input("\nSelect Option: ")

        if choice == '1':
            # Logic for calculation
            crop_name = input("Enter Crop Name: ")
            crops = db.get_all_crops()
            default_crops = crops.get(crop_name.lower(), {})
            
            try:
                area = float(input("Land Area (Acres): "))
                
                # Helper to get default_crops safely
                def_crop = default_crops.get('default_cost_per_acre', 0)
                def_yield = default_crops.get('default_expected_yield', 0)
                def_price = default_crops.get('default_price', 0)

                # Ask user for input, press enter to use default
                input_cost = input(f"Cost/Acre (Default {def_crop}): ")
                cost = float(input_cost) if input_cost else def_crop
                
                input_yield = input(f"Yield/Acre (Default {def_yield}): ")
                yield_value = float(input_yield) if input_yield else def_yield
                
                input_price = input(f"Price/Quintal (Default {def_price}): ")
                price = float(input_price) if input_price else def_price
                
                result = ProfitCalculator.calculate(area, cost, yield_value, price)
                
                if result:
                    print("\n---FINAL RESULTS ---")
                    print(f"Total Revenue: ₹{result['total_revenue']:,.2f}")
                    print(f"Total Cost:    ₹{result['total_cost']:,.2f}")
                    # Color-coded output simulation for CLI
                    if result['net_profit'] >= 0:
                         print(f"Net Profit:    ₹{result['net_profit']:,.2f} (PROFIT)")
                    else:
                         print(f"Net Loss:      ₹{abs(result['net_profit']):,.2f} (LOSS)")
                else:
                    print(" Please enter valid data.")
                
            except ValueError:
                print("Invalid Input. Please enter numbers only.")

        elif choice == '2':
            print("\n--- ADD NEW CROP ---")
            try:
                name = input("Name: ")
                cost = float(input("Cost/Acre: "))
                y= float(input("Yield/Acre: "))
                p = float(input("Price/Quintal: "))
                success, msg = db.add_new_crop(name, cost, y, p)
                if success:
                    print(f"Success: {msg}")
                else:
                    print(f"Error: {msg}")
            except ValueError:
                print("Error: Please enter valid numbers for cost, yield, and price.")

        elif choice == '3':
            print("\n--- RUNNING TESTS ---")
            import unittest
            # Run the tests from testing.py
            tests = unittest.TestLoader().discover('.', pattern='testing.py')
            unittest.TextTestRunner(verbosity=2).run(tests)

        elif choice == '4':
            print("Exiting...")
            sys.exit()

if __name__ == "__main__":
    main()