#--------------------------------------------------------------------------
# Name:  Brandon Burton
# Final Project
# Date: 8 August 2024
#--------------------------------------------------------------------------
#   Main Project Form:  FinalProject_BB.py is where the application holds
#   details about its main flow and functionality.  This is the code that 
#   will execute when starting the applicaion.
#  
#--------------------------------------------------------------------------


from BikeRental import BikeRental, Customer
from RentalManager import RentalManager
from datetime import datetime, timedelta

from BikeRental import BikeRental, Customer
from RentalManager import RentalManager
from datetime import datetime, timedelta

def main():
    # Gather input to set up the bike shop inventory
    print("Welcome to the Bike Rental Shop Setup!")
    
    try:
        intMountainBikes = int(input("Enter the number of mountain bikes available: "))
        intRoadBikes = int(input("Enter the number of road bikes available: "))
        intTouringBikes = int(input("Enter the number of touring bikes available: "))
    except ValueError:
        print("Invalid input. Please enter integer values for the number of bikes.")
        return
    
    # Initialize the bike rental shop with the specified inventory
    objBikeRentalShop = BikeRental(stock={
        'mountain': intMountainBikes,
        'road': intRoadBikes,
        'touring': intTouringBikes
    })
    
    # Create RentalManager instance
    objRentalManager = RentalManager(objBikeRentalShop)

    while True:
        print("\n--- Bike Rental Shop ---")
        print("1. New Customer Rental")
        print("2. Rental Return")
        print("3. Show Inventory")
        print("4. End of Day")
        print("5. Exit Program")

        strChoice = input("Please select an option: ")

        if strChoice == "1":
            # Prompt and validate the customer's name
            while True:
                strName = input("Enter the customer's first and last name: ")
                if not strName.replace(' ', '').isalpha():
                    print("Error: Name must contain only alphabetic characters and spaces.")
                else:
                    break

            # Continuously prompt the user for a unique customer ID
            while True:
                strIDNumber = input("Enter the customer's ID number: ")
                if any(objC.strIDNumber == strIDNumber for objC in objRentalManager.lstCustomers):
                    print(f"Error: A customer with ID {strIDNumber} already exists. Please use a unique ID.")
                else:
                    break


            # Prompt and validate the bike type
            while True:
                strBikeType = input("Enter the type of bike (mountain, road, touring): ").lower()
                if strBikeType not in ['mountain', 'road', 'touring']:
                    print("Invalid bike type. Please choose 'mountain', 'road', or 'touring'.")
                else:
                    break

            # Prompt and validate the number of bikes
            while True:
                try:
                    intQuantity = int(input("Enter the number of bikes: "))
                    if intQuantity <= 0:
                        print("Please enter a positive number.")
                    elif intQuantity > objBikeRentalShop.stock[strBikeType]:
                        print(f"Sorry, we only have {objBikeRentalShop.stock[strBikeType]} {strBikeType} bikes available.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter an integer value.")

            # Prompt and validate the rental basis
            while True:
                strRentalBasis = input("Enter the rental basis (hourly, daily, weekly): ").lower()
                if strRentalBasis not in ['hourly', 'daily', 'weekly']:
                    print("Invalid rental basis. Please choose 'hourly', 'daily', or 'weekly'.")
                else:
                    break

            strCoupon = input("Do you have a coupon code? (y/n): ").lower()
            strCouponCode = input("Enter your coupon code: ") if strCoupon == 'y' else None
            objRentalManager.new_customer_rental(strName, strIDNumber, strBikeType, intQuantity, strRentalBasis, strCouponCode)

        elif strChoice == "2":
            strIDNumber = input("Enter the customer's ID number: ")
            objRentalManager.process_return(strIDNumber)

        elif strChoice == "3":
            objRentalManager.show_inventory()

        elif strChoice == "4":
            objRentalManager.end_of_day_report()

        elif strChoice == "5":
            print("Thank you for using the Bike Rental Shop. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
# Test cases
def run_tests():
    print("\nRunning test cases...\n")
    
    # Initialize the bike rental shop with a fixed inventory
    bike_rental_shop = BikeRental(stock={'mountain': 10, 'road': 8, 'touring': 5})
    rental_manager = RentalManager(bike_rental_shop)

    # Test Case 1: Single Customer Hourly Rental
    customer1 = Customer(strName="Alice", strIDNumber="C001")
    rental_manager.new_customer_rental("Alice", "C001", "mountain", 2, "hourly")
    customer1 = next(c for c in rental_manager.lstCustomers if c.strIDNumber == "C001")
    customer1.dtRentalTime -= timedelta(hours=3)  # Simulate 3 hours rental
    rental_manager.process_return("C001")

    # Test Case 2: Single Customer Daily Rental with Coupon
    customer2 = Customer(strName="Bob", strIDNumber="C002")
    rental_manager.new_customer_rental("Bob", "C002", "road", 3, "daily", "SAVE10BBP")
    customer2 = next(c for c in rental_manager.lstCustomers if c.strIDNumber == "C002")
    customer2.dtRentalTime -= timedelta(days=2)  # Simulate 2 days rental
    rental_manager.process_return("C002")

    # Test Case 3: Family Rental with Weekly Basis
    customer3 = Customer(strName="Charlie", strIDNumber="C003")
    rental_manager.new_customer_rental("Charlie", "C003", "touring", 4, "weekly")
    customer3 = next(c for c in rental_manager.lstCustomers if c.strIDNumber == "C003")
    customer3.dtRentalTime -= timedelta(weeks=1)  # Simulate 1 week rental
    rental_manager.process_return("C003")


    # Final inventory check
    print("\nFinal Inventory:")
    rental_manager.show_inventory()

    # End of Day report
    rental_manager.end_of_day_report()

if __name__ == "__main__":
    # main()
    run_tests()
