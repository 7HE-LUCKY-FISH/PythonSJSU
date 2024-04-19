menu = {
    1: {"item": "Green Beret Omelette", "price": "$12.99"},
    2: {"item": "Get to the Chopped Salad", "price": "$14.99"},
    3: {"item": "Pump You Up Protein Shake", "price": "$9.99"},
    4: {"item": "I'll Be Baby Back Ribs", "price": "$22.99"},
    5: {"item": "Let Off Some Steamed Vegetables", "price": "$4.99"},
    6: {"item": "The Ice Cream Cometh", "price": "$15.99"}
}

key = int(input("Please select your item:\n"))
if (int(key) < 1 or int(key) > 6):
    print("Invalid selection. Please try again. \n")
    key = int(input("Please select your item:\n"))
    #isOrdering = True
    
m1 = menu[key]
quan = int(input("Enter quantity: \n"))
q = {"quantity":quan}
m1.update(q)
menu.update({key: m1})
print(f"Item: {menu[key]['item']}, Price: {menu[key]['price']}, Quantity: {menu[key]['quantity']}")

print("Updated Menu:")
for key, value in menu.items():
    print(f"Item: {value['item']}, Price: {value['price']}, Quantity: {value.get('quantity', 0)}")
