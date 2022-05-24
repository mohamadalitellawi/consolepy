from math import prod
import db
from buisness import Product,LineItem,Cart

def show_title():
    print("The Shopping Cart Program")
    print()

def show_menu():
    print("COMMAND MENU")
    print("cart - show the cart")
    print("add - add an item to the cart")
    print("del - Delete an item from cart")
    print("exit = Exit Program")

def show_products(products):
    print ("PRODUCTS")

    print(f"{'Item':<6}{'Name':<25}{'Price':>10}{'Discount':>10}{'Your Price':>12}")

    for i , product in enumerate(products,start=1):
        print(f"{i:<6d}{product.name:<25}"
                f"{product.price:>10.2f}"
                f"{product.discountPercent:>9d}%"
                f"{product.discountPrice:>12.2f}")
        print()

def show_cart(cart):
    if cart.count == 0:
        print("There are no items in your cart.\n")
    else:
        print(f"{'Item':<6}{'Name':<25}{'Your Price':>12}{'Quantity':>10}{'Total':>10}")

        for i, item in enumerate(cart, start=1):
            print(f"{i:<6d}{item.product.name:<25}{item.product.discountPrice:>12.2f}{item.quantity:>10d}{item.total:>10.2f}")

def get_int(prompt, maxNum = 1000):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Invalid whole number (integer). please try again./n")
            continue
        if number < 1 or number > maxNum:
            print("That number is out of range. Please try again.\n")
        else:
            return number


def add_item(cart, products):
    number = get_int("Item number: ", len(products))
    quantity = get_int("Quantity: ")

    product = products[number-1]
    item = LineItem(product, quantity)
    cart.addItem(item)

    print(f"Item {cart.count} was added.\n")

def remove_item(cart):
    number = get_int("Item Number: ", cart.count)

    cart.removeItem(number-1)
    print(f"Item {cart.count} was deleted.\n")


def main():
    show_title()
    show_menu()

    products = db.get_products()
    show_products(products)


    cart = Cart()

    while True:
        command = input("Command: ").lower()
        if command == "cart":
            show_cart(cart)
        elif command == "add":
            add_item(cart,products)
        elif command == "del":
            remove_item(cart)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not Valid Command. Please try again.\n")

if __name__ == "__main__":
    main()