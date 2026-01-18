# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
def apply_discount(prices):
    prices_copy = prices.copy()
    for idx in range(len(prices_copy)):
        if prices[idx] > 2.00:
            prices[idx] -= prices[idx] * 10 / 100
    return 
updated_prices = apply_discount(product_prices)