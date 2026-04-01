# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for item in products:
    key = item
    associated_values = products.get(item)
    price = float(associated_values[0])
    quantity_sold = int(associated_values[1])
    total_sales = price * quantity_sold
    total_sales_list.append(total_sales)

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
keys = list(products)
for i in range(len(keys)):
    print(f"Total sales for {keys[i]}: ${total_sales_list[i]}")
print('Total sum of all sales: $', total_sum)
print("Minimum sales: $", min_sales)
print("Maximum sales: $", max_sales)