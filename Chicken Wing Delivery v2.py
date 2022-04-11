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

#Delivery Menu
def delivery_menu():

    #Name Input
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name'])

    #Phone Number Input
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

    #House Number Input
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

    #Street Name Input
    question = ("Please enter your Street name ")
    customer_details['street name'] = not_blank(question )
    print (customer_details['street name'])

    #Suburb Name Input
    question = ("Please enter the name of your Subrub ")
    customer_details['suburb'] = not_blank(question )
    print (customer_details['suburb'])


delivery_menu()
print(customer_details)
