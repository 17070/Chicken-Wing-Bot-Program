#Chicken Wing Bot Program
 
import random
from random import randint

#Customer Details Dictionary
customer_details = {}


#Lists
bot_names = ["Turkey Joe jr", "Chunky", "Philip",
             "Bertha", "Agatha", "Jean Phillipe",
             "Felix", "Gertha", "Susan", "Ann"] #List of names to be randomly used for a Bot Name

#Constants
ph_low = 7
ph_high = 10

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
                print(f"Please print a number between {ph_low} and {ph_high}")
        except ValueError:
            print("That is not a valid number")
            print(f"Please print a number between {ph_low} and {ph_high}")


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
                    print("Collect") #Prints Collect when 1 is inputted
                    break

                elif collect_deliver == 2:
                    print("Delivery") #Prints Delivery when 2 is inputted
                    break

            else:
                print("Number must be 1 or 2") 

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")


#Click/Collect Menu
def collect_menu():  
    question = ("Please enter your name ")
    customer_details['name'] = letter_only(question)
    print (customer_details['name'])

        
    question = ("Please enter your phone number ")
    customer_details['phone'] = number_only(question, ph_low, ph_high)
    print (customer_details['phone'])
    print(customer_details)

def confirm_order(): 
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


#Delivery Inputs
#Chicken Wing Menu
#Chicken Wing Order
#Print Receipt
#Cancel Order
#New Order
#Quit Order

#Main
def main ():

    welcome()
    col_del()
    collect_menu()
    confirm_order()
    
main()