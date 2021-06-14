import os
from typing import Literal
from dotenv import load_dotenv
from pandas.core.frame import DataFrame as df
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

# Enable emailed receipts
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

# Loading tax rate env variable  
tax_rate = float(os.getenv("TAXRATE"))

# Importing pandas and reading csv file  
from pandas import read_csv
csv_filepath = (r"C:\Users\jacob\Documents\GitHub\shopping-cart\data\products.csv") #> For some reason, this only started working when I added the 'r' prefix to the file path
products_df = read_csv(csv_filepath)
products_dict = df.to_dict(products_df, "records") #> This took me an embarassingly long time to figure out- to get the df in a format that the selected_products function below would loop through, but I got there!

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

### Info capture

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
        product_ids.append(product_id)

### Info output

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

## Email receipt - Believe this is working as I get a 202 code, although SendGrid flagged my account for review so all my outgoing emails are labeled as "processing"

email_option = input("WOULD YOU LIKE AN EMAILED RECEIPT? (Y/N):")
if email_option == "Y":
    # this must match the test data structure
    template_data = {
        "total_price_usd": to_usd(grand_total),
        "human_friendly_timestamp": checkout_time,
        "products": selected_products
    } 
    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
    message.template_id = SENDGRID_TEMPLATE_ID
    message.dynamic_template_data = template_data
    print("MESSAGE:", type(message))

    try:
        response = client.send(message)
        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)
