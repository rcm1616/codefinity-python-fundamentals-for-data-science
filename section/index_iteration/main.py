prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i == 0:
        discount = 0.1
    elif i == 1:
        discount = 0.2
    elif i == 2:
        discount = 0.15
    elif i == 3:
        discount = 0.05
    prices[i] -= prices[i] * discount
    print(f"Updated price for item {i}: {prices[i]:.2f}:")
    