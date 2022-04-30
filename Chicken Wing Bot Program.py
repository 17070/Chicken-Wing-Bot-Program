#Chicken Wing Bot Program

#Imports
import sys  #Imports the sys module
import random  #Imports the random module
from random import randint #Imports the randint module from the random module

#Lists
#List of names to be randomly used for a Bot Name
bot_names = ["Turkey Joe jr", "Chunky", "Philip",
             "Bertha", "Agatha", "Jean Phillipe",
             "Felix", "Gertha", "Susan", "Ann"]

#List of food items to be used in the Menu Function
menu_items = ['Singular Chicken Wing','100 pack of Chicken Wings',
              'Boned Chicken Wing Burger', 'Potato Burger', 
              'Turkey Chicken Wings', 'Chicken Wing Bones',
              'Chook in a Blanket','Chicken Wing Pizza', 'Chicken Grease Soda',
              'Chicken Wing Ice Cream', 'Turkey Joes Special Monkey Meat Meal',
              'Chicken Wing Fries', 'ChickenCakes']  

#List of prices to be used alongside the menu items in the Menu Function
menu_cost = [1.00, 78.00, 8.00, 8.00, 5.00, 3.50, 8.00, 
             14.00, 3.50, 3.00, 5.00, 3.50, 4.00,]  

#List of menu descriptions used to describe the menu items and is also used in the Menu Function
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

#List to store menu items
order_list = []  
#List to store order cost
order_cost = []  

#Constants
ph_low = 7  #Constant used to establish that ph_low is equal to 7
ph_high = 10  #Constant used to establish that ph_high is equal to 10
house_num_low = 1  #Constant used to establish that house_num_low is equal to 1
house_num_high = 4  #Constant used to establish that house_num_high is equal to 4

#Functions
#Blank Input Function   
#Used for when inputs are inputted as blank
def not_blank(question): 
    valid = False  
    while not valid:  #Sets up while loop
        response = input(question)  #Asks for input
        if response !="":  #Checks for blank input
            return response.title()  #If input is not blank it returns the response to title class 
        else:
            print("This cannot be blank")  #If input is blank prints error message

#Letter Only Function
#Used for when inputs need only words inputted
def letter_only(question):
    while True:  #Sets up while loop
        response = input(question)  #Asks for input
        x = response.isalpha()  #Sets x to true if alpha 
        if x == False: 
            print("Input must only contain letters ") #If x is false prints error message
        else:
            return (response.title())  #If x is true returns the response to title class
            

#Phone Number Validator Function

def number_only(question, ph_low, ph_high):
    while True:  #Sets up while loop
        try:
            num = int(input(question))  #Asks for input and sets input to integer
            test_num = num
            count = 0  #Sets count to 0
            while test_num > 0:  #Sets up while loop
                test_num = test_num//10
                count = count + 1  #Adds 1 to count
            if count >= ph_low and count <= ph_high:  #Checks to see if count is between ph_low and ph_high
                return str(num)  #Returns string back to num when True
            else:
                print(f"Please print a number between {ph_low} and {ph_high}") #Prints error message when False
        except ValueError:
            print("That is not a valid number")
            print(f"Please print a number between {ph_low} and {ph_high}") #Prints error message when ValueError

#House Number Validator Function
def house_number_only(question, house_num_low, house_num_high):
    while True:  #Sets up while loop
        try:
            num = int(input(question))  #Asks for input and sets input to integer
            test_num = num
            count = 0  #Sets count to 0
            while test_num > 0:  #Sets up while loop
                test_num = test_num//10
                count = count + 1  #Adds 1 to count
            if count >= house_num_low and count <= house_num_high:  #Checks to see if count is between house_num_low and house_num_high
                return str(num)  #Returns string back to num when True
            else:
                print(f"Please print a number between {house_num_low} and {house_num_high} digits")  #Prints error message when False
        except ValueError:
            print("That is not a valid number")
            print(f"Please print a number between {house_num_low} and {house_num_high} digits")  #Prints error message when ValueError

#Confirm Order Function for collect menu
def confirm_order_col(): 
    while True:  #Sets up while loop
        try:
            print("")
            print("Is this order correct?")
            print("Enter 1 for yes")
            print("Enter 2 for no")
            confirm_order = int(input("Please enter a number: "))  #Asks for input and sets input to integer

            if confirm_order >= 1 and confirm_order <= 2: #Checks to see if confirm_order is between 1 and 2
                if confirm_order == 1: 
                    print("Order confirmed")
                    print("A text message will be sent to your phone when your order is ready to be collected") 
                    break  #Exits out of loop

                elif confirm_order == 2:
                    print("")
                    collect_menu()  #Runs the collect_menu() function

            else:
                print("Number must be 1 or 2")  #Prints error message when False

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ") #Prints error message when ValueError

#Confirm Order Function for delivery menu
def confirm_order_del(): 
    while True:  #Sets up while loop
        try:
            print("")
            print("Is this order correct?") 
            print("Enter 1 for yes")
            print("Enter 2 for no")
            confirm_order = int(input("Please enter a number: "))  #Asks for input and sets input to integer

            if confirm_order >= 1 and confirm_order <= 2:  #Checks to see if confirm_order is between 1 and 2
                if confirm_order == 1:
                    print("Confirmed Input")
                    break  #Exits out of loop

                elif confirm_order == 2:
                    print("")
                    delivery_menu()  #Runs the delivery_menu() function

            else:
                print("Number must be 1 or 2")  #Prints error message when False

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")  #Prints error message when ValueError

#Confirm Order Function for order menu
def confirm_order_menu(): 
    while True:  #Sets up while loop
        try:
            print("")
            print("Is this order correct?") 
            print("Enter 1 for yes")
            print("Enter 2 for no")
            confirm_order = int(input("Please enter a number: "))  #Asks for input and sets input to integer

            if confirm_order >= 1 and confirm_order <= 2:  #Checks to see if confirm_order is between 1 and 2
                if confirm_order == 1:
                    print("Confirmed Input")
                    print("")
                    break  #Exits out of loop

                elif confirm_order == 2:
                    print("")
                    order()
                    break  #Exits out of loop
            else:
                print("Number must be 1 or 2")  #Prints error message when False

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")  #Prints error message when ValueError

#Delivery Charge Function
def delivery_charge():

    if order_type == "delivery" and num_items < 5:
        order_list.append("Delivery Charge")
        order_cost.append (9) #Adds 9 to the order cost when the order_type is delivery and is greater then 5 items
        print("Because you ordered under 5 menu items there is a delivery charge of $9.00 ")

    elif order_type == "delivery": 
        order_list.append("Delivery Charge")
        order_cost.append (0) #Adds 0 to the order cost


#Confirm Order Function for End of Program
def confirm_order_final(): 
    while True:  #Sets up while loop
        try:
            print("") 
            print("Is this order correct?") 
            print("Enter 1 for yes")
            print("Enter 2 for no")
            confirm_order = int(input("Please enter a number: "))  #Asks for input and sets input to integer

            if confirm_order >= 1 and confirm_order <= 2:  #Checks to see if confirm_order is between 1 and 2
                if confirm_order == 1:
                    print("Order Confirmed")
                    print("Your order has been sent to the kitchen")
                    print("")
                    new_or_exit() #Runs new_or_exit function

                elif confirm_order == 2:
                    print("Your order has been canceled")
                    print("")
                    new_or_exit() #Runs new_or_exit function
                   
            else:
                print("Number must be 1 or 2")  #Prints error message when False

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")  #Prints error message when ValueError


def new_or_exit():
    print("You can place a new order or exit the program")
    print("To start a new order press 1 ")
    print("To exit the program press 2 ")
    while True:  #Sets up while loop
        try:
            confirm = int(input("Please enter a number: "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print("New Order")
                    order_list.clear() #Clears order_list of any stored items
                    order_cost.clear() #Clears order_cost of any stored items
                    customer_details.clear() #Clears customer_details of any stored items
                    main() #Runs main function

                elif confirm == 2:
                    print("Exit Program")
                    order_list.clear() #Clears order_list of any stored items
                    order_cost.clear() #Clears order_cost of any stored items
                    customer_details.clear()  #Clears customer_details of any stored items
                    sys.exit()  #Exits out of program
                    
                else:
                    print("Number must be 1 or 2")  #Prints error message when False

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")  #Prints error message when ValueError

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
    global order_type #Converts order_type from local variable to a global variable
    order_type = ""
    print("Do you want your chicken wings delievered or to collect from store?") 
    print("")
    print("Enter 1 to pick up from store")
    print("Enter 2 if you want your food delivered") 
    print("") 

    while True:  #Sets up while loop
        try:
            collect_deliver = int(input("Please enter a number: ")) #Input Statement asking to input 1 or 2

            if collect_deliver >= 1 and collect_deliver <= 2:
                if collect_deliver == 1:
                    order_type = "collect"
                    print("Collect") #Prints Collect when 1 is inputted
                    collect_menu()  #Runs the collect_menu function
                    break  #Exits out of loop

                elif collect_deliver == 2:
                    order_type = "delivery"
                    print("Delivery") #Prints Delivery when 2 is inputted
                    delivery_menu()  #Runs the delivery_menu function
                    break  #Exits out of loop
            else:
                print("Number must be 1 or 2")  #Prints error message when False

        except ValueError:
            print ("That is not a valid number ")  
            print ("Please enter 1 or 2 ")  #Prints error message when ValueError
    return order_type

#Click/Collect Menu
def collect_menu():  
    question = ("Please enter your name ")  #Sets statement as question
    customer_details['name'] = letter_only(question)  #runs statement through letter_only funtion
    print (customer_details['name']) #prints input

        
    question = ("Please enter your phone number ")  #Sets statement as question
    customer_details['phone'] = number_only(question, ph_low, ph_high) #runs statement through number_only funtion
    print (customer_details['phone']) #prints input
    print(customer_details)  #prints customer details
    confirm_order_col()  #runs the confirm_order_col function
    

#Delivery Menu
def delivery_menu():
    question = ("Please enter your Name: ")  #Sets statement as question
    customer_details['name'] = letter_only(question)  #runs statement through letter_only funtion   
    print (customer_details['name'])  #prints input


    question = ("Please enter your Phone Number: ")  #Sets statement as question
    customer_details['phone'] = number_only(question, ph_low, ph_high) #runs statement through number_only funtion
    print (customer_details['phone'])  #prints input


    question = ("Please enter your House Number: ")  #Sets statement as question
    customer_details['house number'] = house_number_only(question, house_num_low, house_num_high) #runs statement through number_only funtion
    print (customer_details['house number'])  #prints input

    question = ("Please enter your Street Name: ")  #Sets statement as question
    customer_details['street'] = letter_only(question)  #runs statement through letter_only funtion    
    print (customer_details['street'])  #prints input

    question = ("Please enter the name of your suburb: ")  #Sets statement as question
    customer_details['suburb'] = letter_only(question)  #runs statement through letter_only funtion     
    print (customer_details['suburb'])  #prints input
    print(customer_details)  #prints customer details
    confirm_order_col()  #runs the confirm_order_col function

#Chicken Wing Menu
def menu():
    table = []  #List to store table information
    count = 0  #Sets count to 0
    print("{: <13} {: <40} {: <6} {: >15} ".format("Number", "Item", "Cost", "Description"))  #Formats space between headers in the table
    print("------------------------------------------------------------------------------------------------------------------------------------")
    while count in range(len(menu_items)):
        table.append([count+1,menu_items[count], menu_cost[count], menu_description[count]]) #Appends items into the table list
        count = count + 1  #Adds 1 to count
    for row in table:
        print("{: <12} {: <40} ${: <10.2f} {: <100} ".format(*row)) #Formats space between information in the table


#Chicken Wing Order
def order():
    
    global num_items  #Makes the num_items variable global instead of local
    num_items = 0  #Makes num_items 0
    while True:  #Sets up while loop
        try:
            num_items = int(input("How many items would you like to order? ")) #Asks for input and sets input to integer

            if num_items >= 1 and num_items <= 10: #Checks to see if num_items is between 1 and 10
                    print (num_items) #prints num_items
                    break  #Exits out of loop
            else:
                print("Your order must be between 1 and 10 ") #Prints error message if False
            
        except ValueError:
            print("That is not a valid number")
            print("Please enter a number between 1 and 10 ") #Prints error message if ValueError

    #Choose Item
    for item in range (num_items):
        while num_items > 0: 
            while True:  #Sets up while loop
                try:
                    items_ordered = int(input("Please choose your order by entering the menu item number from the menu "))  #Asks for input and sets input to integer
                    if items_ordered >= 1 and items_ordered <= 13:  #Checks to see if num_items is between 1 and 13
                        break  #Exits out of loop
                    else:
                        print("Your order must be between 1 and 13 ")  #Prints error message if False
                except ValueError:
                    print("That is not a valid number")
                    print("Your order must be between 1 and 13 ")  #Prints error message if ValueError
            items_ordered = items_ordered - 1  #Takes away 1 from the items_ordered variable
            order_list.append (menu_items[items_ordered])  #Appends to order_list
            order_cost.append (menu_cost[items_ordered])  #Appends to order_cost
            print("{} ${:.2f}" .format (menu_items[items_ordered], menu_cost[items_ordered]))  #Formats printed items
            num_items = num_items - 1

        

#Print Order Receipt

def receipt(order_type):

    if order_type == "collect":
        print("Your order is for Click and Collect ")
        print("")
        print("Customer Details:")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
        print("")

    elif order_type == "delivery" and num_items < 5:
        print("Your order is for Delivery ")
        print("")
        print("Customer Details:")
        print(f"\n Customer Name: {customer_details['name']} \n Customer Phone: {customer_details['phone']} \n Customer Adress: {customer_details['house number']} {customer_details['street']}, {customer_details['suburb']}")
        print("")

    
    count = 0  #Sets count to 0
    for item in order_list:
        print("\n Ordered: {} \n Cost: ${:.2f}".format (item, order_cost[count]))
        count = count + 1 #Adds 1 to count

    delivery_charge()  #Runs the delivery_charge function
    total_cost = sum(order_cost)  #Makes total cost equal to the sum of the order_cost list
    print("")
    print("Total order cost: ")
    print(f"${total_cost:.2f}") #Prints total cost

#Main
def main ():

    welcome()
    order_type = col_del()
    menu()
    order()
    receipt(order_type)
    confirm_order_final()

main() #Runs the main function