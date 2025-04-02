#Budgetizer

# This is what I made without the extra integer check stuff.

def loop_back():
    print("Let's find out how much money you get to burn!")
    try:
        math_mode = str(input("Do you want to go detailed (D) or rough (R): "))
    except ValueError:
        print("Sorry, can you put in D or R only?")
        loop_back()
        return
    if math_mode == "R":
        money_month = int(input("How much do you take home a month? (numbers only) "))
        money_bills = int(input("How much are your bills every month? "))
        print("You can burn", money_month - money_bills, "円")
    if math_mode == "D":
        money_month = int(input("How much do you take home a month? (numbers only) "))
        money_phone = int(input("How much is your phone bill every month? "))
        money_water = int(input("Your water bill? "))
        money_electric = int(input("Your electric? "))
        money_food = int(input("Your food costs? "))
        money_etc = int(input("Anything else I forgot? "))
        money_bills = money_phone + money_water + money_electric + money_food + money_etc
        print()
        print("You can burn", money_month - money_bills, "円")
        print()
               
    
    start_over = input("Go again? Y or N: ")
    if start_over.upper() == "Y":
        loop_back()
    else:
        print("Okay, bye! Enjoy your partying!")
        

# Call the function to start the loop
loop_back()