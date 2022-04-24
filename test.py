
'''
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


question = ("Please enter your phone number ")

ph_low = 7
ph_high = 10

def number_only(question):
    while True:
        try:
            num = int(input(question))
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


print("Is this order correct?") 
print("Enter 1 for yes")
print("Enter 2 for no") 
while True:
    try:
        confirm_order = int(input("Please enter a number: "))

        if confirm_order >= 1 and confirm_order <= 2:
            if confirm_order == 1:
                print("Order confirmed")
                print("A text message will be sent to your phone when your order is ready to be collected")
                break

            elif confirm_order == 2:
                collect_menu()

        else:
            print("Number must be 1 or 2") 

    except ValueError:
        print ("That is not a valid number ")
        print ("Please enter 1 or 2 ")
'''