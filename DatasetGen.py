import pandas as pd
import random
from faker import Faker
import datetime

fake = Faker()

items = [
    ("Traditional Dress", "Clothes"),
    ("Western Suit", "Clothes"),
    ("Leather Shoes", "Shoes"),
    ("High Heels", "Shoes"),
    ("Designer Bag", "Bags"),
    ("Backpack", "Bags"),
    ("Perfume - Floral", "Perfume"),
    ("Perfume - Woody", "Perfume"),
    ("Sunglasses", "Glasses"),
    ("Reading Glasses", "Glasses"),
    ("Gold Necklace", "Jewelry"),
    ("Diamond Earrings", "Jewelry"),
    ("T-Shirt", "Clothes"),
    ("Jeans", "Clothes"),
    ("Sneakers", "Shoes"),
    ("Sandals", "Shoes"),
    ("Handbag", "Bags"),
    ("Clutch", "Bags"),
    ("Perfume - Citrus", "Perfume"),
    ("Perfume - Oriental", "Perfume"),
    ("Eyeglasses", "Glasses"),
    ("Designer Watch", "Jewelry"),
    ("Formal Shirt", "Clothes"),
    ("Skirt", "Clothes"),
    ("Running Shoes", "Shoes"),
    ("Boots", "Shoes"),
    ("Leather Wallet", "Bags"),
    ("Tote Bag", "Bags"),
    ("Perfume - Fresh", "Perfume"),
    ("Perfume - Spicy", "Perfume"),
    ("Diamond Ring", "Jewelry")
]

coupon_names = ["SAVE10", "DISCOUNT20", "FREESHIP", "GET50OFF", "SALE25"]
customer_dict = {}
domain_names = ["gmail.com", "yahoo.com", "outlook.com", "example.com", "hotmail.com"]
num_samples = 300000
output_file = "Sales Data.csv"
for sample_number in range(num_samples):
    customer_name = fake.name() #name
    email = fake.unique.email() #email
    if email in customer_dict: #existing customer emails (will change to IDs)
        customer_id = customer_dict[email]["Customer ID"]
        customer_name = customer_dict[email]["Customer Name"]
    else:
        customer_id = random.randint(1000, 9999)
        customer_dict[email] = {"Customer ID": customer_id, "Customer Name": customer_name}

    order_date = fake.date_time_between_dates(datetime_start=datetime.datetime(2023, 2, 1), datetime_end=datetime.datetime(2023, 12, 31))
    ordered_items = random.sample(items, random.randint(0, 20))
    item_type = [item[1] for item in ordered_items]
    total_bill = sum(random.uniform(5, 50) for _ in ordered_items)
    actual_cost = sum(random.uniform(1, 10) for _ in ordered_items)
    tax = total_bill * random.uniform(0.05, 0.15)
    net_profit = total_bill - actual_cost - tax

    if not ordered_items:
        mode_of_shopping = None
        coupon_code = None
    else:
        mode_of_shopping = random.choice(["Ship-to-Address", "BOPIS", "Ship-to-Store", "POS"])
        coupon_code = random.choice(coupon_names)

    product_prices = [round(random.uniform(5, 50), 2) for _ in ordered_items]

    sample_data = pd.DataFrame({
        "Customer ID": [customer_id],
        "Customer Name": [customer_name],
        "Email": [email],
        "Order Date": [order_date],
        "Ordered Items": [ordered_items],
        "Item Type": [item_type],
        "Total Bill": [total_bill],
        "Actual Cost": [actual_cost],
        "Tax": [tax],
        "Net Profit": [net_profit],
        "Mode of Shopping": [mode_of_shopping],
        "Coupon Code": [coupon_code],
        "Product Prices": [product_prices]
    })

    if sample_number == 0:
        sample_data.to_csv(output_file, index=False)
    else:
        sample_data.to_csv(output_file, mode="a", header=False, index=False)
