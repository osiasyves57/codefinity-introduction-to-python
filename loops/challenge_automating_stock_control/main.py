# Grocery store inventory:
# "Item": [current stock, target stock level, restock amount]
inventory = {
    "Bread": [30, 50, 10],
    "Eggs": [120, 200, 40],
    "Milk": [60, 100, 20],
    "Apples": [15, 50, 15]
}

# Grocery store inventory:
# "Item": [current stock, target stock level, restock amount]
inventory = {
    "Bread": [30, 50, 10],
    "Eggs": [120, 200, 40],
    "Milk": [60, 100, 20],
    "Apples": [15, 50, 15]
}

print("Restocking started")

# Write your code here
for item in inventory:
    print(f"Restocking {item}")
    # unpack current, target, restock
    current, target, amt = inventory[item]
    while current < target:
        current += amt
    inventory[item][0] = current

print("Restocking completed")
