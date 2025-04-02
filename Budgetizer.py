# Budgetizer

#The first def get_integer_input section is something I looked up to simplify
#checking every input for being an integer or not. Without it, all the "get_integer_input"
#parts just go away and it should still work, it just won't throw up errors for non-integers.
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Oops! Please enter a valid integer.")

#loop_back is a variable that I defined so it will start back at the beginning. The name can be anything
#but loop_back was the most easily understandable for me lol.

def loop_back():
    print()
    print("Let's find out how much money you get to burn!")

    while True:
        math_mode = input("Do you want to go detailed (D) or rough (R): ").upper()
        
#I had to look up this "in [range]" part too. It seems really useful though.

        if math_mode in ['R', 'D']:
            break
        else:
            print("Invalid input. Please enter either 'R' or 'D'.")

    print()

    if math_mode == "R":
        money_month = get_integer_input("How much do you take home a month? (numbers only) ")
        money_bills = get_integer_input("How much are your bills every month? ")
        print()
        print("You can burn", money_month - money_bills, "円")
        print()
        if (money_month - money_bills) <30000:
            print("Whoa buddy. Don't think you should be partying...")
        elif (money_month - money_bills) <70000:
            print("Is there anywhere you can cut some costs?")
        elif (money_month - money_bills) >70000:
            print("Wow! You can party AND save some money too! Good job, you!")
    elif math_mode == "D":
        money_month = get_integer_input("How much do you take home a month? (numbers only) ")
        money_rent = get_integer_input("How much is your rent? ")
        money_phone = get_integer_input("How much is your phone bill every month? ")
        money_water = get_integer_input("Your water bill? ")
        money_electric = get_integer_input("Your electric? ")
        money_food = get_integer_input("Your food costs? ")
        money_etc = get_integer_input("Anything else I forgot? ")
        money_bills = money_rent + money_phone + money_water + money_electric + money_food + money_etc
        print()
        print("You can burn", money_month - money_bills, "円")
        print()
        if (money_month - money_bills) <=30000:
            print("Whoa buddy. Don't think you should be partying...")
        elif (money_month - money_bills) <=50000:
            print("Is there anywhere you can cut some costs?")
        elif (money_month - money_bills) >50000:
            print("Wow! You can party AND save some money too! Good job, you!")
    print()
    start_over = input("Go again? Y or N: ").upper()
    if start_over == "Y":
        loop_back()
    else:
        print("Okay, bye! Enjoy your partying!")

# Call the function to start the loop
loop_back()
