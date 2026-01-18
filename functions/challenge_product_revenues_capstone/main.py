# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
revenue = [i*j for i,j in zip(prices, quantities_sold)]
revenue_per_product = list(zip(products, revenue))
print(revenue)


def calculate_revenue(prices, quantities_sold):
    revenues = []
    for i,j in zip(prices, quantities_sold):
        revenue.append(i*j)
    return revenues
        
def print_revenue(revenues):
 sorted(revenues)
 for product_name, revenue in revenues:
    print(f"{product_name} has total revenue of ${revenue}")

calculate_revenue(prices, quantities_sold)
print_revenue(revenue_per_product)

