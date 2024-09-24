#Define the menu of cafe
menu = {
'Pizza': 120,
'Burger': 75,
'Hot coffee': 40,
'Cold coffee':55,
'Fries': 40,
'Cold drink':30,
'chocolate shake' :75,
'Tea' : 25,
'Paneer Sandwiches' : 65,
'Onion Sandwiches' : 75,
'Corn Sandwiches' : 70,
'Pastries' : 30,
'Chocolate icecream': 20,
'Vanilla icecream' : 25,
'Salads' : 25,
'Soups'  : 20,
}
#Greet
print("Welcome to Minicafe")
print("Pizza: Rs 120")
print("Burger: Rs 75")
print("Hot coffee: Rs 40")
print("Cold coffee: Rs 55")
print("Fries: Rs 40")
print("Cold drink: Rs 30")
print("Chocolate shake: Rs 75")
print("Tea: Rs 25")
print("Paneer Sandwiches: Rs 65")
print("Onion Sandwiches: Rs 75")
print("Corn Sandwiches: Rs 70")
print("Pastries: Rs 30")
print("Chocolate icecream: Rs 20")
print("Vanilla icecream: Rs 25")
print("Salads: Rs 25")
print("Soups: Rs 20")




print("Welcome to Minicafe")
for item, price in menu.items():
    print(f"{item}: Rs {price}")

# Initialize order total
order_total = 0

# Loop to add items to the order
while True:
    item = input("What do you want to order? ").strip()
    if item in menu:
        order_total += menu[item]
        print(f"Your order {item} has been added.")
    else:
        print(f"Ordered item {item} is not available.")

    another_order = input("Do you want to add another item? (Yes/No) ").strip().lower()
    if another_order != "yes":
        break

# Display the total order amount
print(f"The total amount to pay is Rs {order_total}.")