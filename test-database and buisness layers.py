import db
from buisness import Product, LineItem, Cart

products = db.get_products()
product = products[1]

lineItem = LineItem(product,2)
cart = Cart()
cart.addItem(lineItem)

print(f"Product:\t{product.name}")
print(f"Price:\t{product.discountPrice}")
print(f"Quantity:\t{lineItem.quantity}")
print(f"Total:\t{cart.total}")