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
                    'Chicken burger served with tomatos, lettuce, cheese, and wing sauce',
                    'Potato based pattie served with tomatos, lettuce, cheese, and wing sauce',
                    'Fried turkey wings made from turkey',
                    'Chicken Finger Fries made with chicken',
                    'Pita wrap with fresh chicken, tomatos, lettuce, and dressing',
                    'Fried Chicken and cheese served on a wing sauce base', 
                    'Vanilla flavoured Cream soda',
                    'Flavoured ice cream covered in a crumbed coating',
                    'Kids meal with a chicken wing burger, a small serving of fries, and Juice',
                    'Crinkle-Cut fries seasoned with chicken salt',
                    'Fried Chicken Nuggets']

def menu():
    table = []
    count = 0
    print("{: <13}{: <40}{: <4} {:<10}".format("Number", "Item", "Cost", "Description"))
    print("-----------------------------------------------------------------------------------------------------")
    while count in range(len(menu_items)):
        table.append([count+1,menu_items[count], menu_cost[count], menu_description[count]])
        count = count + 1
    for row in table:
        print("{: <12} {: <40} ${: <10.2f} {: <80} ".format(*row))


menu()