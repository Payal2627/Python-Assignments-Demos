#Default argument concept
#It starts from left to right
#right to left not allowed
def sum(x=0,y=0,z=0):
    return x+y+z

x= int(input("Enter a number : "))
y= int(input("Enter a number : "))
z = int(input("Enter a number : "))
s = sum(x,y,z)
print("Sum =",s)
s = sum(x,y)
print("Sum =",s)
s = sum(x)
print("Sum =",s)
s = sum()
print("Sum =",s)


def display(eid,ename,basic):
    print("Eid =",eid)
    print("EName = ",ename)
    print("Basic = ",basic)


display(basic=32000,eid=101,ename="Akshay")


#Keyword Argument

def display(**kwargs):
    print(kwargs)


display(eid=101,ename="Akshay",salary=32000)
display(sid=101,sname="Rahul",percentage=78,age=12)
display(bid=101,bname="Let us C",price=600,author='Kanetkar')



x = 10
y = 10

print(id(x))
print(id(y))


def sum(*args):
    s = 0
    for x in args:
        s += x
    print("Sum =",s)


sum(10,20)
sum(10,20,30)
sum(10,20,30,40)
sum(10,20,30,40,50)

#Tuple -> Data inside ( )


def factorial(n):
    f = 1
    while n>=1 : 
        f = f*n
        n-=1
    return f

def sum(*args):
    s = 0
    for x in args:
        s += x
    return s

def area_of_circle(radius):
    area = 3.14*radius*radius
    return area

def menu():
    print("\t\t1.Factorial")
    print("\t\t2.Sum")
    print("\t\t3.Area of circle")
    print("\t\t4.Exit")
    

choice = 0
while choice != 4:
    menu()
    choice = int(input("Enter your choice : "))
    if choice == 1:
        num = int(input("Enter a number : "))
        f = factorial(num)
        print("Factorial =",f)
    elif choice == 2:
        x = int(input("Enter first number : "))
        y = int(input("Enter second number : "))
        z = int(input("Enter third number : "))
        s = sum(x,y,z)
        print("Sum =",s)
    elif choice == 3:
        radius = float(input("Enter radius : "))
        area = area_of_circle(radius)
        print("Area = ",area)
    elif choice == 4:
        print("--------end of program-----------")
    
        