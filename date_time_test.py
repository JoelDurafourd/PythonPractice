from datetime import date

def monthToNum(shortMonth):
    return {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9,
            'oct': 10,
            'nov': 11,
            'dec': 12
    }[shortMonth]

year = int(input("Give me a year please "))
month = input("Give me a month please ")
a = date(year, monthToNum(month), 1)
print(a.weekday())

# day_number = (date(year, month + 1, 1) - date(year, month, 1)).days

# # print(day_number)



# print(monthToNum(month))
