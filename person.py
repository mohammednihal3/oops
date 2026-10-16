class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Person Details")
        print("Name:", self.name)
        print("Age:", self.age)


name = input("Enter your name: ")
age = int(input("Enter your age: "))

p1 = Person(name, age)
p1.display_details()