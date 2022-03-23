#Collect or Delivery Menu

print("Do you want your chicken wings delievered or to collect from store?")

print("Enter c to pick up from store or enter d if you want your food delivered")

collect_deliver = input()

if collect_deliver == "d":
    print("delivery")

elif collect_deliver == "c":
    print("collect")

else:
    print("That was not a valid input")


