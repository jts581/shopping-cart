import os
from typing import Literal
from dotenv import load_dotenv
from pandas.core.frame import DataFrame as df
load_dotenv()

# Loading tax rate env variable  
tax_rate = float(os.getenv("TAXRATE"))

# Importing pandas and reading csv file  
from pandas import read_csv
csv_filepath = (r"C:\Users\jacob\Documents\GitHub\shopping-cart\data\products.csv")
products_df = read_csv(csv_filepath)
products_dict = df.to_dict(products_df, "records") #> This took me an embarassingly long time to figure out, to get the df in a format that the selected_products function below would loop through, but I got there!

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

    # Validate item exists
    if product_id not in str(products_df["id"]):
       print("THAT ITEM DOES NOT EXIST, PLEASE ENTER AN ID BETWEEN 1-20 OR DONE")

    else:
        #selected_products = [p for p in products if int(p["id"]) == int(product_id)]
        #selected_product = selected_products[0]
        #total_price = total_price + selected_product["price"]
        #print("Selected product: " + selected_product["name"] + ": " + to_usd(selected_product["price"]))
        product_ids.append(product_id)

### INFO OUTPUT

print("--------------")
print("JAKE'S PY SHOP")
print("www.eatpy.com")
print("--------------")

from datetime import datetime

now = datetime.now()

checkout_time = now.strftime("%m/%d/%y %I:%M:%S %p")

print("CHECKOUT TIME:",checkout_time)
print("--------------")

print("ITEMS: ")
for product_id in product_ids:
        selected_products = [p for p in products_dict if str(p["id"]) == str(product_id)]
        selected_product = selected_products[0]
        total_price = total_price + selected_product["price"]
        print("-",str(selected_product["name"]) + ": " + to_usd(selected_product["price"]))

tax = tax_rate * total_price
grand_total = sum([tax, total_price])

print("--------------")
print("SUBTOTAL: ", to_usd(total_price))
print("TAX: ", to_usd(tax))
print("TOTAL: ", to_usd(grand_total))
print("--------------")
print("THANKS FOR STOPPING PY :)")
print("--------------")

## EMAIL RECEIPT - Ran out of time to get to this

#email_option = input("WOULD YOU LIKE A RECEIPT? (Y/N):")
#    if email_option == "N":
#        break

