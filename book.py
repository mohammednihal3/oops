class books:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print("Enter your book information: ")
        print("book name:", self.title)
        print("Author:", self.author)
        print("price:" ,self.price)
        print("***************")
        
title = input("Enter your title: ")
author = input("Enter author name: ")
price = int(input("Enter the price: "))
    
book1 = books(title,author,price)
book1.display()