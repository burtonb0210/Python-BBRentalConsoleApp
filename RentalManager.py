#--------------------------------------------------------------------------
# Name:  Brandon Burton
# Final Project
# Date: 8 August 2024
#--------------------------------------------------------------------------
#   RentalManager:  RentalManager.py holds some input validation and handles
#   flow for processing rental "utilities".  It holds functionality for 
#   inventory functions as well as new customer functions. 
#   
#--------------------------------------------------------------------------


from BikeRental import Customer

class RentalManager:
    def __init__(self, objBikeRentalShop):
        self.objBikeRentalShop = objBikeRentalShop
        self.lstCustomers = []

    def new_customer_rental(self, strName, strIDNumber, strBikeType, intQuantity, strRentalBasis, strCouponCode=None):
        while True:
            if not strName.replace(' ', '').isalpha():
                print("Error: Name must contain only alphabetic characters and spaces.")
                strName = input("Enter the customer's first and last name: ")
            else:
                break

        while True:
            if any(objC.strIDNumber == strIDNumber for objC in self.lstCustomers):
                print(f"Error: A customer with ID {strIDNumber} already exists. Please use a unique ID.")
                strIDNumber = input("Enter a unique customer ID: ")
            else:
                break

        objCustomer = Customer(strName, strIDNumber)
        self.lstCustomers.append(objCustomer)

        if strCouponCode:
            objCustomer.apply_coupon(strCouponCode)

        objCustomer.rent_bike(self.objBikeRentalShop, intQuantity, strRentalBasis, strBikeType)
        print(f"Rental completed successfully for {objCustomer.strName}.")

    def process_return(self, strIDNumber):
        objReturningCustomer = next((objC for objC in self.lstCustomers if objC.strIDNumber == strIDNumber), None)
        if objReturningCustomer:
            objReturningCustomer.return_bike(self.objBikeRentalShop)
            self.lstCustomers.remove(objReturningCustomer)
        else:
            print("No rental record found for this customer.")

    def show_inventory(self):
        self.objBikeRentalShop.displaystock()

    def end_of_day_report(self):
        print("\n--- End of Day Report ---")
        print(f"Total Bikes Rented Today: {self.objBikeRentalShop.getTotalDailyRentals()}")
        print(f"Daily Revenue Collected Today: ${self.objBikeRentalShop.getTotalDailyRevenue():.2f}")
        print("------------------------------")

        self.objBikeRentalShop.dblDailyRevenue = 0
        self.objBikeRentalShop.intDailyRentals = 0
        print("Daily totals reset. Ready for the next day.")
