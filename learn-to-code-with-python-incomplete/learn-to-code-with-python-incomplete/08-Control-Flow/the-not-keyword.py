def countdown(number): 
    count = 0
    while number >= count:
        print(number)
        number -= 1
        if number <= 0: 
            print("Boom!")
            return

    
countdown(500)