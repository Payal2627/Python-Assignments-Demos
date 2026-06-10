try:
    x = int(input("Enter first number : "))
    y = int(input("Enter first number : "))        
    result = x+y
    print("Result = ",result)  
except:
    print("Something went wrong")
#Finally block is executed whether exception occurs or not
finally:
    print("This is a very very very important code")