#Chicken Wing Order

num_items = 0
while True:
    try:
        num_items = int(input("How many items would you like to order? "))
        if num_items >= 1 and num_items <= 10:
                print (num_items) 
                break
        else:
            print("Your order must be between 1 and 10 ")
        
    except ValueError:
        print("That is not a valid number")
        print("Please enter a number between 1 and 10 ")


