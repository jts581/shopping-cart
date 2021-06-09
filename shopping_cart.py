products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output
#Write a program that asks the user to input one or more product identifiers, then looks up the prices for each, then prints 
# an itemized customer receipt including the total amount owed.

#The program should use one of the provided datastores (see "Data Setup") to represent the store owner's inventory of products 
# and prices.

#The program should prompt the checkout clerk to input the identifier of each shopping cart item, one at a time.

#When the clerk inputs a product identifier, the program should validate it, displaying a helpful message like "Hey, are you 
# sure that product identifier is correct? Please try again!" if there are no products matching the given identifier.

#At any time the clerk should be able to indicate there are no more shopping cart items by inputting the word DONE or otherwise 
# indicating they are done with the process. Before asking for identifiers, the program should provide clear instructions to the user
# about how to use the "DONE" keyword.

#After the clerk indicates there are no more items, the program should print a custom receipt on the screen. The receipt should
# include the following components:
#    A grocery store name of your choice
#    A grocery store phone number and/or website URL and/or address of choice
#    The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
#    The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
#    The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
#    The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
#    The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
#    A friendly message thanking the customer and/or encouraging the customer to shop again

#The program should be able to process multiple shopping cart items of the same kind, but need not display any groupings or 
# aggregations of those items (although it may optionally do so).


### INFO CAPTURE

total_price = 0
product_ids = []

while True:
    product_id = input("Please input the product identifier, or 'DONE' if there are no more items:") #> this is a string
    #> "DONE"
    if product_id == "DONE":
        break
    
    else:
        #matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        #matching_product = matching_products[0]
        #total_price = total_price + matching_product["price"]
        #print("Selected product: " + matching_product["name"] + ": " + to_usd(matching_product["price"]))
        product_ids.append(product_id)
    

#print(product_id)
#print(type(product_id))

### INFO OUTPUT
print("--------------")
print("JAKE'S PY SHOP")
print("www.eatmypy.com")
print("--------------")

from datetime import datetime

now = datetime.now()

checkout_time = now.strftime("%m/%d/%y %I:%M:%S %p")

print("CHECKOUT TIME:",checkout_time)
print("--------------")

print("ITEMS: ")
for product_id in product_ids:
        matching_products = [p for p in products if str(p["id"]) == str(product_id)]
        matching_product = matching_products[0]
        total_price = total_price + matching_product["price"]
        print("-",str(matching_product["name"]) + ": " + to_usd(matching_product["price"]))

print("--------------")
print("SUBTOTAL: " + to_usd(total_price))