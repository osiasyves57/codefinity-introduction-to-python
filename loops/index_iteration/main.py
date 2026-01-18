prices = [29.99, 45.50, 12.75, 38.20]
discount_percentage = [10, 20, 15, 5]

# Write your code here
for i in range(len(prices)):
    prices[i] -= prices[i] * discount_percentage[i] / 100
    print(f"Updated price for item {i}: {prices[i]:.2f}")