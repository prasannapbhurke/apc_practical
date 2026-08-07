cart = ["Milk","Bread"]
cart.append("Eggs")
cart.remove("Bread")
item = input("Search item: ")
print("Found" if item in cart else "Not Found")
print(cart)
print("Total Items:", len(cart))

