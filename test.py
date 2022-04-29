
'''
def letter_only(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters ")
        else:
            return (response.title())
            
question = "Enter your name"
name = letter_only(question)
print(name)


question = ("Please enter your phone number ")

ph_low = 7
ph_high = 10

def number_only(question):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= ph_low and count <= ph_high:
                print(num)
                break
            else:
                print("New Zealand numbers only have between 7 to 10 digits")
        except ValueError:
            print("Please enter a number")


print("Is this order correct?") 
print("Enter 1 for yes")
print("Enter 2 for no") 
while True:
    try:
        confirm_order = int(input("Please enter a number: "))

        if confirm_order >= 1 and confirm_order <= 2:
            if confirm_order == 1:
                print("Order confirmed")
                print("A text message will be sent to your phone when your order is ready to be collected")
                break

            elif confirm_order == 2:
                collect_menu()

        else:
            print("Number must be 1 or 2") 

    except ValueError:
        print ("That is not a valid number ")
        print ("Please enter 1 or 2 ")


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
                    '100 frozen chicken wings in one bundle (Take Away Only)',
                    'Crispy chicken burger served with tomatos, lettuce, cheese, and wing sauce',
                    'Potato based pattie served with tomatos, lettuce, cheese, and wing sauce',
                    'Fried turkey wings made from turkey',
                    'Chicken Finger Fries made with chicken',
                    'Pita wrap with fresh chicken, tomatos, lettuce, and dressing',
                    'Fried Chicken and cheese served on a wing sauce base', 
                    'Vanilla flavoured Cream soda',
                    'Flavoured ice cream covered in a crumbed coating',
                    'Kids meal including a chicken wing burger, a small serving of fries, and Juice',
                    'Crinkle-Cut fries seasoned with chicken salt',
                    'Fried Chicken Nuggets']


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
        table.append([count+1,menu_items[count], menu_cost[count], menu_description[count]])
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
        order_list.append(menu_items[items_ordered])
        order_cost.append(menu_cost[items_ordered])
        print("{} ${:.2f}" .format (menu_items[items_ordered], menu_cost[items_ordered]))
        num_items = num_items - 1

print("")
for order_list, order_cost in zip(order_list, order_cost):
    print("{} ${:.2f}" .format (order_list,order_cost))


#Lists
bot_names = ["Turkey Joe jr", "Chunky", "Philip",
             "Bertha", "Agatha", "Jean Phillipe",
             "Felix", "Gertha", "Susan", "Ann"] #List of names to be randomly used for a Bot Name

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

customer_details = {}

order_list = []

order_cost = []


#Chicken Wing Menu
def menu():
    table = []
    count = 0
    print("{: <13} {: <40} {: <6} {: >15} ".format("Number", "Item", "Cost", "Description"))
    print("------------------------------------------------------------------------------------------------------------------------------------")
    while count in range(len(menu_items)):
        table.append([count+1,menu_items[count], menu_cost[count], menu_description[count]])
        count = count + 1
    for row in table:
        print("{: <12} {: <40} ${: <10.2f} {: <100} ".format(*row))

#Chicken Wing Order
def order():
    
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
    print("Menu items ordered: ")
    for order_list, order_cost in zip(order_list, order_cost):
        print("{} ${:.2f}" .format (order_list,order_cost))

#Print Order Receipt
def receipt(order_type):
  
    total_cost = sum(order_cost)

    if order_type == "collect":
        print("Your order is for Click and Collect ")
        print("")
        print("Customer Details:")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
        print("")

    elif order_type == "delivery":
        print("Your order is for Delivery ")
        print("")
        print("Customer Details:")
        print(f"Customer Name: {customer_details['name']} \n Customer Phone: {customer_details['phone']} \n Customer Adress: {customer_details['house number']} {customer_details['street']}, {customer_details['suburb']}")
        print("")

 
    
    count = 0
    for item in order_list:
        print("\n Ordered: {} \n Cost: ${:.2f}".format (item, order_cost[count]))
        count = count + 1

    print("")
    print("Total order cost: ")
    print(f"${total_cost:.2f}")


def delivery_charge():

    if order_type == "delivery" and num_items < 5:
        order_list.append("Delivery Charge")
        order_cost.append (9)

    elif order_type == "delivery": 
        total_cost = total_cost + 9 
        order_list.append("Delivery Charge")
        order_cost.append (0)
'''