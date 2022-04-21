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
            

#Click/Collect Menu

def collect_menu():  
    question = ("Please enter your name ")
    customer_details['name'] = letter_only(question )
    print (customer_details['name'])

        
    valid = False
    while not valid:
        try:
            customer_details['phone'] = int(input("Please enter your Phone Number "))
            if customer_details['phone'] != "":
                print(customer_details['phone'])
                break   
            else:
                print("This cannot be blank")
        except ValueError:
            print("Please enter numbers only")
            
collect_menu()
print(customer_details)
print("A text message will be sent to your phone when your order is ready to be collected")