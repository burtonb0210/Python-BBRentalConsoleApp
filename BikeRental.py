#--------------------------------------------------------------------------
# Name:  Brandon Burton
# Final Project
# Date: 8 August 2024
#--------------------------------------------------------------------------
#   BikeRental:  BikeRental.py stores both the BikeRental class and the
#   Customer class.  This is the form where minor updates were made to add
#   new functionality for the console application.
#   
#--------------------------------------------------------------------------

from datetime import datetime

class BikeRental:
    def __init__(self, stock=None):
        if stock is None:
            stock = {'mountain': 0, 'road': 0, 'touring': 0}
        self.stock = stock
        self.dblDailyRevenue = 0
        self.intDailyRentals = 0

    def displaystock(self):
        print("\n--- Bike Inventory ---")
        print(f"Mountain Bikes: {self.stock['mountain']}")
        print(f"Road Bikes: {self.stock['road']}")
        print(f"Touring Bikes: {self.stock['touring']}")
        print("----------------------")
        return self.stock

    def rentBike(self, strBikeType, intN, strRentalBasis):
        if strBikeType not in self.stock:
            print(f"Sorry, we don't have {strBikeType} bikes.")
            return None

        if intN <= 0:
            print("Number of bikes should be positive!")
            return None

        if intN > self.stock[strBikeType]:
            print(f"Sorry! We have currently {self.stock[strBikeType]} {strBikeType} bikes available to rent.")
            return None

        dtNow = datetime.now()
        self.stock[strBikeType] -= intN
        self.intDailyRentals += intN

        strFormattedTime = dtNow.strftime("%I:%M %p")
        
        if strRentalBasis == "hourly":
            print(f"You have rented {intN} {strBikeType} bike(s) on hourly basis today at {strFormattedTime}.")
            print("You will be charged $5 for each hour per bike.")
            return dtNow
        elif strRentalBasis == "daily":
            print(f"You have rented {intN} {strBikeType} bike(s) on daily basis today at {strFormattedTime}.")
            print("You will be charged $20 for each day per bike.")
            return dtNow
        elif strRentalBasis == "weekly":
            print(f"You have rented {intN} {strBikeType} bike(s) on weekly basis today at {strFormattedTime}.")
            print("You will be charged $60 for each week per bike.")
            return dtNow
        else:
            print("Invalid rental basis. Please choose 'hourly', 'daily', or 'weekly'.")
            return None

    def returnBike(self, strBikeType, dtRentalTime, strRentalBasis, intN, blnApplyDiscount=False):
        dtRentalEndTime = datetime.now()
        dtRentalDuration = dtRentalEndTime - dtRentalTime

        if strRentalBasis == "hourly":
            dblTotalHours = dtRentalDuration.total_seconds() / 3600
            dblBill = dblTotalHours * 5 * intN
        elif strRentalBasis == "daily":
            dblTotalDays = dtRentalDuration.total_seconds() / (3600 * 24)
            dblBill = dblTotalDays * 20 * intN
        elif strRentalBasis == "weekly":
            dblTotalWeeks = dtRentalDuration.total_seconds() / (3600 * 24 * 7)
            dblBill = dblTotalWeeks * 60 * intN

        if 3 <= intN <= 5:
            print("Family rental promotion applied!")
            dblBill *= 0.75

        if blnApplyDiscount:
            print("Coupon discount applied!")
            dblBill *= 0.9

        print(f"Total bill for returning {intN} {strBikeType} bike(s): ${dblBill:.2f}")

        self.stock[strBikeType] += intN
        self.dblDailyRevenue += dblBill

    def getTotalDailyRentals(self):
        return self.intDailyRentals

    def getTotalDailyRevenue(self):
        return self.dblDailyRevenue


class Customer:
    def __init__(self, strName, strIDNumber):
        self.strName = strName
        self.strIDNumber = strIDNumber
        self.dtRentalTime = None
        self.lstBikesRented = []
        self.strRentalBasis = None
        self.strCouponCode = None

    def see_available_bikes(self, objBikeRentalShop):
        return objBikeRentalShop.displaystock()

    def rent_bike(self, objBikeRentalShop, intN, strRentalBasis, strBikeType):
        self.dtRentalTime = objBikeRentalShop.rentBike(strBikeType, intN, strRentalBasis)
        if self.dtRentalTime:
            self.lstBikesRented = [strBikeType] * intN
            self.strRentalBasis = strRentalBasis

    def apply_coupon(self, strCouponCode):
        if strCouponCode.endswith("BBP"):
            print("Coupon code applied successfully!")
            self.strCouponCode = strCouponCode
        else:
            print("Invalid coupon code.")

    def return_bike(self, objBikeRentalShop):
        if self.dtRentalTime and self.lstBikesRented:
            dtRentalEndTime = datetime.now()
            dtRentalDuration = dtRentalEndTime - self.dtRentalTime

            if self.strRentalBasis == "hourly":
                dblTotalHours = dtRentalDuration.total_seconds() / 3600
                dblBill = dblTotalHours * 5 * len(self.lstBikesRented)
            elif self.strRentalBasis == "daily":
                dblTotalDays = dtRentalDuration.total_seconds() / (3600 * 24)
                dblBill = dblTotalDays * 20 * len(self.lstBikesRented)
            elif self.strRentalBasis == "weekly":
                dblTotalWeeks = dtRentalDuration.total_seconds() / (3600 * 24 * 7)
                dblBill = dblTotalWeeks * 60 * len(self.lstBikesRented)

            if 3 <= len(self.lstBikesRented) <= 5:
                print("Family rental promotion applied!")
                dblBill *= 0.75

            if self.strCouponCode:
                print("Coupon discount applied!")
                dblBill *= 0.9

            print(f"Thank you for returning the bikes. Your total bill is ${dblBill:.2f}.")
            objBikeRentalShop.stock[self.lstBikesRented[0]] += len(self.lstBikesRented)
            objBikeRentalShop.dblDailyRevenue += dblBill
            self.dtRentalTime = None
            self.lstBikesRented = []
            self.strRentalBasis = None
            self.strCouponCode = None
        else:
            print("You have no bikes to return.")

