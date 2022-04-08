#Chicken Wing Bot Program
 
import random
from random import randint

#Lists
bot_names = ["Turkey Joe jr", "Chunky", "Philip",
             "Bertha", "Agatha", "Jean Phillipe",
             "Felix", "Gertha", "Susan", "Ann"]


#Welcome
def welcome ():
    num = randint(0,9)
    name = (bot_names[num])

    print("")
    print("***Welcome to Turkey Joe's Chicken Wingeria***")
    print("***My name is",name,"***")
    print("***I will be here to help you order your chicken wings***")
    print("")

#Main
def main ():

    welcome()

main()


#Pickup or Delivery
#Pickup Inputs
#Delivery Inputs
#Chicken Wing Menu
#Chicken Wing Order
#Print Receipt
#Cancel Order
#New Order
#Quit Order