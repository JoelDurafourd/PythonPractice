# Define a divisible_by_three_and_four function that accepts a number as its argument. 
# It should return True if the number is evenly divisible by both 3 and 4 . 
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True
def divisible_by_three_and_four(number): 
    if ((number % 3) == 0) and ((number % 4) == 0): 
        return True
    else: 
        return False

print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))


print()
print("1", 1 % 3)
print("2", 2 % 3)
print("3", 3 % 3)
print("4", 4 % 3)
print("5", 5 % 3)
print("6", 6 % 3)
print("7", 7 % 3)
print("8", 8 % 3)
print("9", 9 % 3)
print("10", 10 % 3)
print("11", 11 % 3)
print("12", 12 % 3)
print()
print("1", 1 % 4)
print("2", 2 % 4)
print("3", 3 % 4)
print("4", 4 % 4)
print("5", 5 % 4)
print("6", 6 % 4)
print("7", 7 % 4)
print("8", 8 % 4)
print("9", 9 % 4)
print("10", 10 % 4)
print("11", 11 % 4)
print("12", 112 % 4)