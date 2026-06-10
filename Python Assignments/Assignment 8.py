'''Python Assignment -8 (Functions)'''

#Question 1) Write a program to calculate area of rectangle
def rectangle_area(length, breadth):
    area = length * breadth
    return area

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
result = rectangle_area(length, breadth)
print("Area of Rectangle =", result)


#Question 2) Write a program to calculate area of circle
def circle_area(radius):
    area = 3.14 * radius * radius
    return area
radius = float(input("Enter radius: "))
result = circle_area(radius)
print("Area of Circle =", result)


#Question 3) Write a program to find sum of following series using functions :
#a) 1+ 2 + 3 + 4+..... + n
def series_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter value of n: "))
result = series_sum(n)
print("Sum =", result)


#3b) 1!+ 2! + 3! + 4!+..... + n!
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i

    return fact

def factorial_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + factorial(i)

    return total

n = int(input("Enter value of n: "))
result = factorial_series(n)
print("Sum of factorial series =", result)


#3c) 1^1 + 2^2 + 3^3+ ...... n^n
def power_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + (i ** i)

    return total

n = int(input("Enter value of n: "))
result = power_series(n)
print("Sum =", result)


#Question 4) Sum of all odd numbers between 1 to n
def odd_sum(n):
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total = total + i

    return total

n = int(input("Enter value of n: "))
result = odd_sum(n)
print("Sum of odd numbers =", result)


#Question 5) Sum of all prime numbers between 1 to n
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def prime_sum(n):

    total = 0

    for i in range(1, n + 1):
        if is_prime(i):
            total = total + i

    return total

n = int(input("Enter value of n: "))
result = prime_sum(n)
print("Sum of prime numbers =", result)


#Question 6) Write a program to find print the following Fibonacci series using functions: 1 1 2 3 5 8 n terms
def fibonacci(n):

    a = 1
    b = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c

n = int(input("Enter number of terms: "))
fibonacci(n)


#Question 7) Write a program to find sum of digits of a number.
def digit_sum(num):

    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total

num = int(input("Enter number: "))
result = digit_sum(num)
print("Sum of digits =", result)


#Question 8) Write a program find reverse of a number
def reverse_number(num):

    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

num = int(input("Enter number: "))
result = reverse_number(num)
print("Reverse number =", result)


#Question 9) Write a program to check if entered number is a palindrome or not.
def reverse_number(num):

    reverse = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    return reverse

def palindrome(num):

    if num == reverse_number(num):
        return True
    else:
        return False

num = int(input("Enter number: "))
if palindrome(num):
    print("Palindrome Number")
else:
    print("Not Palindrome")


#Question 10) Write a program to check if entered year is a leap year or not.
def leap_year(year):

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Enter year: "))
if leap_year(year):
    print("Leap Year")
else:
    print("Not Leap Year")


#Question 11) WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def armstrong(num):

    temp = num
    total = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == num:
        return True
    else:
        return False

num = int(input("Enter number: "))
if armstrong(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")