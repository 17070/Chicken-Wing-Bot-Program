#Print Order Receipt

order_list = ['Singular Chicken Wing','100 pack of Chicken Wings',
              'Boned Chicken Wing Burger', 'Potato Burger', ]
order_cost = [1.00, 10.00, 8.00, 8.00]

count = 0
for item in order_list:
    print("Ordered: {} Cost: ${:.2f}".format (item, order_cost[count]))
    count = count + 1
