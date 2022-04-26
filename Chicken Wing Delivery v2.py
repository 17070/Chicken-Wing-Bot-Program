#Customer Details Dictionary
customer_details = {}

#Letter Only Function
def letter_only(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters ")
        else:
            return (response.title())

#Delivery Menu
question = ("Please enter your Name: ") 
customer_details['name'] = letter_only(question)     
print (customer_details['name'])


valid = False
while not valid:
    try:
        customer_details['phone'] = input("Please enter your Phone Number: ")
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
        customer_details['house number'] = input("Please enter your House Number: ")
        if customer_details['house number'] != "":
            print(customer_details['house number'])
            break   
        else:
            print("This cannot be blank")
    except ValueError:
        print("Please enter numbers only")

question = ("Please enter your Street Name: ") 
customer_details['Street'] = letter_only(question)     
print (customer_details['Street'])

question = ("Please enter the name of your suburb: ") 
customer_details['Suburb'] = letter_only(question)     
print (customer_details['Suburb'])


print(customer_details)
