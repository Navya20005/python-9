class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price")

    def display_details(self):
        print("Product Name:", self.name)
        print("Price:", self.__price)


product = Product("Laptop", 50000)

product.display_details()

product.price = 55000

print("\nAfter Price Update:")
product.display_details()

product.price = 0