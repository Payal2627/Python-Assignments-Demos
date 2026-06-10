'''Python Assignment on OOP'''

'''
Q1
Create a class Book with members as bid,bname,price and author.Add following
methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor
c. ShowBook
'''
class Book:
    def __init__(self, bid=0, bname="", price=0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def ShowBook(self):
        print("Book ID :", self.bid)
        print("Book Name :", self.bname)
        print("Price :", self.price)
        print("Author :", self.author)

    def __del__(self):
        print("Book Object Destroyed")


b1 = Book(101, "Python Programming", 500, "ABC")
b2 = Book()

print("Book 1 Details")
b1.ShowBook()

print("\nBook 2 Details")
b2.ShowBook()

'''
Q2
Create a class Product with members as pid,pname,price and quantity .Add
following methods:
d. Constructor (Support both parameterized and parameterless)
e. Destructor
f. ShowBook
'''
class Product:
    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def ShowProduct(self):
        print("Product ID :", self.pid)
        print("Product Name :", self.pname)
        print("Price :", self.price)
        print("Quantity :", self.quantity)

    def __del__(self):
        print("Product Object Destroyed")

p1 = Product(1, "Laptop", 50000, 5)
p2 = Product()

print("Product 1 Details")
p1.ShowProduct()

print("\nProduct 2 Details")
p2.ShowProduct()

'''
Q3
Create a class Shirt with members as sid,sname,type(formal etc), price and
size(small,large etc) .Add following methods:
g. Constructor (Support both parameterized and parameterless)
h. Destructor
i. ShowBook
'''
class Shirt:
    def __init__(self, sid=0, sname="", stype="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def ShowShirt(self):
        print("Shirt ID :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type :", self.stype)
        print("Price :", self.price)
        print("Size :", self.size)

    def __del__(self):
        print("Shirt Object Destroyed")

s1 = Shirt(201, "Arrow", "Formal", 1200, "Large")
s2 = Shirt()

print("Shirt 1 Details")
s1.ShowShirt()

print("\nShirt 2 Details")
s2.ShowShirt()