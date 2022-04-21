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
            
question = "Enter your name"
name = letter_only(question)
print(name)

#Phone Number Validator Function
def number_only(question):
    while True:
        try:
            num = int(input(question, ph_low, ph_high))
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

#Click/Collect Menu

def collect_menu():  
  question = ("Please enter your name ")
  customer_details['name'] = not_blank(question )
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