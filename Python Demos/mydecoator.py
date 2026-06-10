def mydecorator(func):
    def wrapper():
        print("Welcome all")
        func()
        print("Thankyou")
    return wrapper

@mydecorator
def fun1():    
    print("I am fun1")
    
@mydecorator
def fun2():    
    print("I am fun2")
    
@mydecorator
def fun3():    
    print("I am fun3")
    
# result = mydecorator(fun3)
# result()

fun1()
fun2()
fun3()