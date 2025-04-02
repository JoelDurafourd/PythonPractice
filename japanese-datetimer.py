import csv
import os

month = "default"
days_of_month = 31
user_input_month = input("Please enter your month (jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec) ").lower()
user_input_day = input("Please enter the first day of that month (sun, mon, tue, wed, thu, fri, sat) ").lower()

if user_input_month == "feb":
    leap_year = input("is it a leapyear? y/n ")
    if leap_year == "y":
        days_of_month = 29
    else:
        days_of_month = 28
elif user_input_month == "apr" or "jun" or "sep" or "nov":
    days_of_month = 30

def day_week_int_convert(number):
    if number == "mon":
        return 1
    elif number == "tue":
        return 2
    elif number == "wed":
        return 3
    elif number == "thu":
        return 4
    elif number == "fri":
        return 5
    elif number == "sat":
        return 6
    elif number == "sun":
        return 7
    else:
        return "Invalid input"

def day_week_conversion(number):
    if number == 1:
        return "月"
    elif number == 2:
        return "火"
    elif number == 3:
        return "水"
    elif number == 4:
        return "木"
    elif number == 5:
        return "金"
    elif number == 6:
        return "土"
    elif number == 7:
        return "日"
    else:
        return "Invalid input"

def weekday_reset(number):
    if number == 7:
        return 1
    else:
        return number + 1

weekday = day_week_int_convert(user_input_day)

print(f"{user_input_month} has {days_of_month} days")

# Prepare data for CSV
csv_data = []

# Generate the day-week pairs and add them to the csv_data list
for i in range(days_of_month):
    day_week_pair = f"{i + 1} {day_week_conversion(weekday)}"
    csv_data.append([day_week_pair])  # Add each pair in a new column
    weekday = weekday_reset(weekday)

# Define the file path
file_path = f"{user_input_month}_days.csv"

# Print the file path for debugging purposes
print(f"Saving to: {os.path.abspath(file_path)}")

# Write data to a CSV file with UTF-8 encoding
with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Days of the Month"])  # Optional header
    writer.writerows(csv_data)

print(f"CSV file '{file_path}' has been created.")
