class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
length = float(input("Enter the length:"))
width = float(input("Eter the width:"))

rect = rectangle(length,width)
print("Area of the rectangle :", rect.area())