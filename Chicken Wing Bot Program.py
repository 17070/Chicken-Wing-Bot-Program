#Chicken Wing Bot Program
 
import random
from random import randint



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

#Customer Details Dictionary
customer_details = {}


order_list = []

order_cost = []

#Constants
ph_low = 7
ph_high = 10
house_num_low = 1
house_num_high = 4

#Functions
#Blank Input Function      
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response !="":
            return response.title()
        else:
            print("This cannot be blank")   

#Letter Only Function
def letter_only(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters ")
        else:
            return (response.title())
            

#Phone Number Validator Function
def number_only(question, ph_low, ph_high):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= ph_low and count <= ph_high:
                return str(num)
            else:
                print(f"Please print a number between {ph_low} and {ph_high} digits")
        except ValueError:
            print("That is not a valid number")
            print(f"Please print a number between {ph_low} and {ph_high} digits")

#House Number Validator Function
def house_number_only(question, house_num_low, house_num_high):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= house_num_low and count <= house_num_high:
                return str(num)
            else:
                print(f"Please print a number between {house_num_low} and {house_num_high} digits")
        except ValueError:
            print("That is not a valid number")
            print(f"Please print a number between {house_num_low} and {house_num_high} digits")

#Confirm Order Function for collect menu
def confirm_order_col(): 
    while True:
        try:
            print("")
            print("Is this order correct?") 
            print("Enter 1 for yes")
            print("Enter 2 for no")
            confirm_order = int(input("Please enter a number: "))

            if confirm_order >= 1 and confirm_order <= 2:
                if confirm_order == 1:
                    print("Order confirmed")
                    print("A text message will be sent to your phone when your order is ready to be collected")
                    break

                elif confirm_order == 2:
                    print("")
                    collect_menu()

            else:
                print("Number must be 1 or 2") 

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")

#Confirm Order Function for delivery menu
def confirm_order_del(): 
    while True:
        try:
            print("")
            print("Is this order correct?") 
            print("Enter 1 for yes")
            print("Enter 2 for no")
            confirm_order = int(input("Please enter a number: "))

            if confirm_order >= 1 and confirm_order <= 2:
                if confirm_order == 1:
                    print("Order confirmed")
                    break

                elif confirm_order == 2:
                    print("")
                    delivery_menu()

            else:
                print("Number must be 1 or 2") 

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")

#Confirm Order Function for order menu
def confirm_order_menu(): 
    while True:
        try:
            print("")
            print("Is this order correct?") 
            print("Enter 1 for yes")
            print("Enter 2 for no")
            confirm_order = int(input("Please enter a number: "))

            if confirm_order >= 1 and confirm_order <= 2:
                if confirm_order == 1:
                    print("Order confirmed")
                    break

                elif confirm_order == 2:
                    print("")
                    order()
                    break
            else:
                print("Number must be 1 or 2") 

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")


#Welcome
def welcome ():
    num = randint(0,9) #Picks a random number between 0 and 9 
    name = (bot_names[num]) #Uses random number to pick a Bot name from the Bot Name List

    print("")
    print("* * * Welcome to Turkey Joe's Chicken Wingeria * * *")
    print("* * * My name is",name," * * *")
    print("* * * I will be here to help you order your chicken wings * * *")
    print("") #Printed Welcome to the User using random Bot Name


#Collect or Delivery Menu
def col_del():
    order_type = ""
    print("Do you want your chicken wings delievered or to collect from store?") 
    print("")
    print("Enter 1 to pick up from store")
    print("Enter 2 if you want your food delivered") 
    print("") #Printed Questions and Statements to User

    while True:
        try:
            collect_deliver = int(input("Please enter a number: ")) #Input Statement asking to input 1 or 2

            if collect_deliver >= 1 and collect_deliver <= 2:
                if collect_deliver == 1:
                    order_type = "collect"
                    print("Collect") #Prints Collect when 1 is inputted
                    collect_menu()
                    break

                elif collect_deliver == 2:
                    order_type = "delivery"
                    print("Delivery") #Prints Delivery when 2 is inputted
                    delivery_menu()
                    break
            else:
                print("Number must be 1 or 2") 

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")
    return order_type

#Click/Collect Menu
def collect_menu():  
    question = ("Please enter your name ")
    customer_details['name'] = letter_only(question)
    print (customer_details['name'])

        
    question = ("Please enter your phone number ")
    customer_details['phone'] = number_only(question, ph_low, ph_high)
    print (customer_details['phone'])
    print(customer_details)
    confirm_order_col()
    

#Delivery Menu
def delivery_menu():
    question = ("Please enter your Name: ") 
    customer_details['name'] = letter_only(question)     
    print (customer_details['name'])


    question = ("Please enter your Phone Number: ")
    customer_details['phone'] = number_only(question, ph_low, ph_high)
    print (customer_details['phone'])


    question = ("Please enter your House Number: ")
    customer_details['house number'] = house_number_only(question, house_num_low, house_num_high)
    print (customer_details['house number'])

    question = ("Please enter your Street Name: ") 
    customer_details['street'] = letter_only(question)     
    print (customer_details['street'])

    question = ("Please enter the name of your suburb: ") 
    customer_details['suburb'] = letter_only(question)     
    print (customer_details['suburb'])
    print(customer_details)
    confirm_order_col()

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
            order_list.append (menu_items[items_ordered])
            order_cost.append (menu_cost[items_ordered])
            print("{} ${:.2f}" .format (menu_items[items_ordered], menu_cost[items_ordered]))
            num_items = num_items - 1

    print("")
    print("Menu items ordered: ")
    for order_list, order_cost in zip(order_list, order_cost):
        print("{} ${:.2f}" .format (order_list,order_cost))
    confirm_order_menu()

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

#Cancel Order
#New Order
#Quit Order

#Main
def main ():

    welcome()
    order_type = col_del()
    menu()
    order()
    receipt(order_type)

main()