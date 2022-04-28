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

#Main
def main ():

    order_type = col_del()
    print (order_type)
    
main()

'''
#Print Order Receipt
def receipt():
    order_list = ['Singular Chicken Wing','100 pack of Chicken Wings',
                'Boned Chicken Wing Burger', 'Potato Burger', ]
    order_cost = [1.00, 10.00, 8.00, 8.00]

    customer_details = {'Name': 'Dante', 'Phone': '2340987','House Number': '34', 'Street': 'Cherry' , 'Suburb': 'Howick'}

    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format (item, order_cost[count]))
        count = count + 1
        '''