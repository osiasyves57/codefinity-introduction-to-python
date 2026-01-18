# Products and their current stock
products = [["Apples", 10], ["Bananas", 8]]

# Units sold today (same order as products)
units_sold = [3, 5]

for prod in range(len(products)):
    products[prod][1] -= units_sold[prod]
    print("Final stock levels: ", products)
    