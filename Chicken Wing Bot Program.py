#Chicken Wing Bot Program
 
import random
from random import randint

#Lists
bot_names = ["Turkey Joe jr", "Chunky", "Philip",
             "Bertha", "Agatha", "Jean Phillipe",
             "Felix", "Gertha", "Susan", "Ann"] #List of names to be randomly used for a Bot Name

#Functions


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



#Pickup Inputs
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

main()