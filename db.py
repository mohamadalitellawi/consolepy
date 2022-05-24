import csv

from buisness import Product

FILENAME = "products.csv"

def get_products():
    products = []
    with open(FILENAME,newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            #Convert row to product object
            product = Product(row[0],float(row[1]),int(row[2]))
            products.append(product)
    return products