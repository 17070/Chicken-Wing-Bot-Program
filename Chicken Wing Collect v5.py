#Customer Details Dictionary
customer_details = {}

#Blank Input         
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response !="":
            return response.title()
        else:
            print("This cannot be blank")   



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