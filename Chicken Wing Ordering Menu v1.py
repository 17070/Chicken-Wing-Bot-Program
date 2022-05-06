<<<<<<< HEAD
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


=======
#List of menu items
menu_items = ['Singular Chicken Wing','100 pack of Chicken Wings',
              'Boned Chicken Wing Burger', 'Potato Burger with Chicken Wing Fries', 
              'Turkish Turkey Chicken Wings', 'Chicken Wing Bones',
              'Turkey Wings','Chicken Wing Pizza', 'Chicken Grease Soda',
              'Chicken Wing Ice Cream', 'Turkey Joes Special Monkey Meat Meal',
              'Chicken Wing Fries', 'ChickenCakes']
>>>>>>> parent of 0f51bf9 (qwa)
