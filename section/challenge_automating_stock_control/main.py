# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started...")
for item in inventory:
    current_stock = inventory.get(item)[0]
    minimum_stock = inventory.get(item)[1]
    restock_quantity = inventory.get(item)[2]
    sale_status = inventory.get(item)[3]
    while current_stock < minimum_stock:
        current_stock += restock_quantity
    inventory[item][0] = current_stock
    if current_stock > discount_threshold:
        inventory[item][3] = True
    print(f"Processing {item}")
print("Processing completed")