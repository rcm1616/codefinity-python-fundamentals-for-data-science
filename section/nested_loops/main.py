produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = []
groceries.append(produce)
groceries.append(dairy)

for i in range(len(groceries)):
    for y in range(len(groceries[i])):
        print(groceries[i][y])
    
