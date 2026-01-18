product_type = "Perishable"
days_in_stock = 8
stock_quantity = 2
if product_type == "Perishable":
 if days_in_stock > 7:
    print("Perishable and very old - Apply 70% discount")
 elif stock_quantity < 3:
     print("perishable and low stock - restock immediately")
 else:
     print("Perishable and fresh - Full price")
elif product_type == "Non-perishable":
    if stock_quantity == 0:
        print("Non-perishable and out of stock - Reorder Now")
    else:
        print("Non-perishable and stock is sufficient")


# Write a nested if-else statement below