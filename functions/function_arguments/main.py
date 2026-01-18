def apply_discount(price, discount=0.10):
    price -= price * discount / 100
    return price

def add_tax(price, tax= 0.05):
    price += price * tax / 100
    return price

def final_price(price, discount=0.10, tax=0.05):
    return add_tax(apply_discount(price,discount))

a = final_price(50)
b = final_price(50, tax=0.08)
print(f"Final price with default discount and tax: {a}")
print(f"Final price with custom tax: {final_price}")
    
