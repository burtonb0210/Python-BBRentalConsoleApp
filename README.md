# Python-BBRentalConsoleApp
Python console application for managing a bike rental shop. Handles inventory, customer rentals, billing, and discount logic.

# Bike Rental Console Application

**Author:** Brandon Burton  
**Date:** August 8, 2024  

A Python console application designed as a final project for college coursework. The app simulates a bike rental shop and includes functionality to manage:

- Bike inventory (mountain, road, touring)
- Customer rentals with unique IDs
- Rental pricing by time basis (hourly, daily, weekly)
- Coupon code validation and family rental discounts
- End-of-day revenue and rental reports
- Robust input validation and test cases

---

## 🚲 Features

- Console-driven user interface
- Input validation for names, bike types, and rental choices
- Support for coupon codes ending in `BBP` (10% off)
- Family rental discount (25% off for 3–5 bikes)
- End-of-day reset function and reporting
- Automated test cases included

---

## 🧰 Technologies Used

- Python 3
- Standard libraries (`datetime`, `timedelta`)
- OOP structure (BikeRental, Customer, RentalManager classes)

---

## 🧪 How to Run

```bash
# Run main app
python FinalProject_BB.py

# Run test cases
python FinalProject_BB.py  # (uncomment run_tests in __main__)
