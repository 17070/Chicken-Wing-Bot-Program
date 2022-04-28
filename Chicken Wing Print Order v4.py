#Collect or Delivery Menu
def col_del():
    order_type = ""
    print("Do you want your chicken wings delievered or to collect from store?") 
    print("")
    print("Enter 1 to pick up from store")
    print("Enter 2 if you want your food delivered") 
    print("") #Printed Questions and Statements to User

    while True:
        try:
            collect_deliver = int(input("Please enter a number: ")) #Input Statement asking to input 1 or 2

            if collect_deliver >= 1 and collect_deliver <= 2:
                if collect_deliver == 1:
                    order_type = "collect"
                    print("Collect") #Prints Collect when 1 is inputted
                    break

                elif collect_deliver == 2:
                    order_type = "delivery"
                    print("Delivery") #Prints Delivery when 2 is inputted
                    break
            else:
                print("Number must be 1 or 2") 

        except ValueError:
            print ("That is not a valid number ")
            print ("Please enter 1 or 2 ")
    return order_type


#Print Order Receipt
def receipt(order_type):
    order_list = ['Singular Chicken Wing','100 pack of Chicken Wings',
                'Boned Chicken Wing Burger', 'Potato Burger', ]
    order_cost = [1.00, 10.00, 8.00, 8.00]

    customer_details = {'Name': 'Dante', 'Phone': '2340987','House Number': '34', 'Street': 'Cherry' , 'Suburb': 'Howick'}

    total_cost = sum(order_cost)

    if order_type == "collect":
        print("Your order is for Click and Collect ")
        print("")
        print("Customer Details:")
        print("\n Customer Name: {} \n Customer Phone: {}" .format(customer_details['Name'], customer_details['Phone']))
        print("")

    elif order_type == "delivery":
        print("Your order is for Delivery ")
        print("")
        print("Customer Details:")
        print("\n Customer Name: {} \n Customer Phone: {} \n Customer House Number: {} \n Customer Street Name: {} \n Customer Suburb Name: {}" .format(customer_details['Name'], customer_details['Phone'], customer_details['House Number'], customer_details['Street'], customer_details['Suburb']))
        print("")

 
    
    count = 0
    for item in order_list:
        print("\n Ordered: {} \n Cost: ${:.2f}".format (item, order_cost[count]))
        count = count + 1

    print("")
    print("Total order cost: ")
    print(f"${total_cost:.2f}")
    
        

#Main
def main ():

    order_type = col_del()
    receipt(order_type)
main()