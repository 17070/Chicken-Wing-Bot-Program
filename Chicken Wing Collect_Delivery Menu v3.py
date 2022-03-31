#Collect or Delivery Menu

def col_del():
    print("Do you want your chicken wings delievered or to collect from store?")

    print("Enter 1 to pick up from store")
    print("Enter 2 if you want your food delivered")

    collect_deliver = int(input("Please enter a number: "))

            
    if collect_deliver == 1:
        print("Collect")
                    

    elif collect_deliver == 2:
        print("Delivery")
                        
    else:
        print("Number must be 1 or 2")

col_del()