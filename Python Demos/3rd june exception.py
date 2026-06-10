try:
    x = int(input("Enter a number : "))
    print("You entered : ",x)
except:
    print("Something went wrong...")

try:
    x = int(input("Enter first number : "))
    y = int(input("Enter first number : "))
    result = x/y    
#Specialized exception handler
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Denomenator must not be zero")
#Generalized exception handler
except:
    print("Something went wrong...")
else:
    #The code which must execute when there is not exception
    print("Result ",result)

try:
    x = int(input("Enter first number : "))
    y = int(input("Enter first number : "))
    try:
        result = x/y    
    except ZeroDivisionError:
        print("Denomenator must not be zero")    
except ValueError:
    print("Please enter a number")
#Generalized exception handler
except:
    print("Something went wrong...")
else:
    #The code which must execute when there is not exception
    print("Result ",result)

try:
    try:
        x = int(input("Enter first number : "))
        y = int(input("Enter first number : "))        
    except ValueError:
        print("Inner block")
        print("Please enter a number")
        raise #re-throw the exception
except ValueError:
    print("Outer block")
    print("Please enter a number")