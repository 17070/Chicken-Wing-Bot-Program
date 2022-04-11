#Customer Details Dictionary
customer_details = {}

#Delivery Menu

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

valid = False
while not valid:
    try:
        customer_details['house number'] = int(input("Please enter your House Number "))
        if customer_details['house number'] != "":
            print(customer_details['house number'])
            break   
        else:
            print("This cannot be blank")
    except ValueError:
        print("Please enter numbers only")

valid = False
while not valid:
    customer_details['street name'] = input("Please enter your Street Name ")     
    if customer_details['street name'] != "":
        print(customer_details['street name'])
        break  
    else:
        print("This cannot be blank")

valid = False
while not valid:
    customer_details['suburb'] = input("Please enter the name of your Suburb ")     
    if customer_details['suburb'] != "":
        print(customer_details['suburb'])
        break  
    else:
        print("This cannot be blank")


print(customer_details)

