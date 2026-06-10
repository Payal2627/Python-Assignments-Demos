#Case 1 : Function with no parameter and no return value
def factorial():
    num = int(input("Enter a number : "))
    f = 1
    while num>=1:
        f = f*num
        num-=1
    print("Factorial =",f)

factorial()


#Case 2 : Function with parameter and no return value
def factorial():    
    f = 1
    while num>=1:
        f = f*num
        num-=1
    print("Factorial =",f)

num = int(input("Enter a number : "))
factorial(num)


#Case 3 : Function with no parameter and return value
def factorial():    
    num = int(input("Enter a number : "))
    f = 1
    while num>=1:
        f = f*num
        num-=1
    return f


result = factorial()
print("Factorial =",result)


#Case 4 : Function with parameter and return value
def factorial(num):        
    f = 1
    while num>=1:
        f = f*num
        num-=1
    return f

num = int(input("Enter a number : "))
result = factorial(num)
print("Factorial =",result)


