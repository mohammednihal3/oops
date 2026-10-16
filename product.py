class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def display_details(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Price:", self.calculate_total())


name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

p1 = Product(name, price, quantity)
p1.display_details()