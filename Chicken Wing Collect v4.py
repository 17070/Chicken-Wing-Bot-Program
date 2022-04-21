#Customer Details Dictionary
customer_details = {}

#Click/Collect Menu
valid = False
while not valid:
    customer_details['name'] = input("Please enter your Name ")     
    if customer_details['name'] != "":
        print(customer_details['name'])
        break  
    else:
        print("This cannot be blank")

 
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

print(customer_details)
print("A text message will be sent to your phone when your order is ready to be collected")