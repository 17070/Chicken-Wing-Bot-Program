#Click/Collect Menu

valid = False
while not valid:
    name = input("Please enter your Name ")     
    if name != "":
        print(name)
        break  
    else:
        print("This cannot be blank")
        

valid = False
while not valid:
    phone = input("Please enter your Phone Number ")
    if phone != "":
        print(phone)
        break   
    else:
        print("This cannot be blank")

print("A text message will be sent to your phone when your order is ready to be collected")

