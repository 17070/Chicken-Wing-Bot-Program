
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


#List of menu items
menu_items = ['Singular Chicken Wing','100 pack of Chicken Wings',
              'Boned Chicken Wing Burger', 'Potato Burger', 
              'Turkey Chicken Wings', 'Chicken Wing Bones',
              'Chook in a Blanket','Chicken Wing Pizza', 'Chicken Grease Soda',
              'Chicken Wing Ice Cream', 'Turkey Joes Special Monkey Meat Meal',
              'Chicken Wing Fries', 'ChickenCakes']

menu_cost = [1.00, 78.00, 8.00, 8.00, 5.00, 3.50, 8.00, 
             14.00, 3.50, 3.00, 5.00, 3.50, 4.00,]

menu_description = ['A single chicken wing',
                    '100 frozen chicken wings in one bundle (Take Away Only)',
                    'Crispy chicken burger served with tomatos, lettuce, cheese, and wing sauce',
                    'Potato based pattie served with tomatos, lettuce, cheese, and wing sauce',
                    'Fried turkey wings made from turkey',
                    'Chicken Finger Fries made with chicken',
                    'Pita wrap with fresh chicken, tomatos, lettuce, and dressing',
                    'Fried Chicken and cheese served on a wing sauce base', 
                    'Vanilla flavoured Cream soda',
                    'Flavoured ice cream covered in a crumbed coating',
                    'Kids meal including a chicken wing burger, a small serving of fries, and Juice',
                    'Crinkle-Cut fries seasoned with chicken salt',
                    'Fried Chicken Nuggets']
'''



data = []

header = data.pop(0)

def column_length(text,length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " * length)[:length]
    return text

for column in header:
    print(column_length(column,20), end = "  ")   

