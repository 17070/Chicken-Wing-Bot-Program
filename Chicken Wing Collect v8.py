#Customer Details Dictionary
customer_details = {}

#Constants
ph_low = 7
ph_high = 10

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

collect_menu()
confirm_order()
