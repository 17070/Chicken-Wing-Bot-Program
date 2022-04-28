#List of menu items

menu_items = ['Singular Chicken Wing','100 pack of Chicken Wings',
              'Boned Chicken Wing Burger', 'Potato Burger', 
              'Turkey Chicken Wings', 'Chicken Wing Bones',
              'Chook in a Blanket','Chicken Wing Pizza', 'Chicken Grease Soda',
              'Chicken Wing Ice Cream', 'Turkey Joes Special Monkey Meat Meal',
              'Chicken Wing Fries', 'ChickenCakes']

menu_cost = [1.00, 78.00, 8.00, 8.00, 5.00, 3.50, 8.00, 
             14.00, 3.50, 3.00, 5.00, 3.50, 4.00,]

menu_description = ['A single chicken wing',
                    '100 frozen chicken wings in one bundle',
                    'Chicken burger served with tomatos, lettuce, cheese, and wing sauce',
                    'Potato pattie served with tomatos, lettuce, cheese, and wing sauce',
                    'Fried turkey wings made from turkey',
                    'Chicken Finger Fries made with chicken',
                    'Pita wrap with fresh chicken, tomatos, lettuce, and dressing',
                    'Fried Chicken and cheese served on a wing sauce base', 
                    'Vanilla flavoured Cream soda',
                    'Flavoured ice cream covered in a crumbed coating',
                    'Kids meal with a chicken wing burger, small serving of fries, and Juice',
                    'Crinkle-Cut fries seasoned with chicken salt',
                    'Fried Chicken Nuggets']

def menu():
    table = []
    count = 0
    print("{: <13} {: <40} {: <6} {: >15} ".format("Number", "Item", "Cost", "Description"))
    print("------------------------------------------------------------------------------------------------------------------------------------")
    while count in range(len(menu_items)):
        table.append([count+1 ,menu_items[count], menu_cost[count], menu_description[count]])
        count = count + 1
    for row in table:
        print("{: <12} {: <40} ${: <10.2f} {: <100} ".format(*row))

menu()


order_list = []
order_cost = []

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

#Choose Item
for item in range (num_items):
    while num_items > 0:
        while True:
            try:
                items_ordered = int(input("Please choose your order by entering the menu item number from the menu "))
                if items_ordered >= 1 and items_ordered <= 13:
                    break
                else:
                    print("Your order must be between 1 and 13 ")
            except ValueError:
                print("That is not a valid number")
                print("Your order must be between 1 and 13 ")
        items_ordered = items_ordered - 1
        order_list.append(menu_items[items_ordered])
        order_cost.append(menu_cost[items_ordered])
        print("{} ${:.2f}" .format (menu_items[items_ordered], menu_cost[items_ordered]))
        num_items = num_items - 1
print("")
for order_list, order_cost in zip(order_list, order_cost):
    print("{} ${:.2f}" .format (order_list,order_cost))