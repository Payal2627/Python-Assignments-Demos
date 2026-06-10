'''Python Assignment -9 (Recursion)'''


'''
Question 1) Write a program to find sum of following series using recursive functions:
i. 1! + 2! + 3! + 4! +..... + n!
Note : For fact and sum two recursive functions
'''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def sum_series(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_series(n - 1)

n = int(input("Enter value of n: "))

result = sum_series(n)

print("Sum of series =", result)


#Q2) Write a program to check if given number is Armstrong or not using recursive function.
def armstrong(num, temp, digits):
    if temp == 0:
        return 0

    digit = temp % 10

    return (digit ** digits) + armstrong(num, temp // 10, digits)

num = int(input("Enter number: "))

digits = len(str(num))

result = armstrong(num, num, digits)

if result == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


#Q3) Write a program to reverse a given number using recursive function.
def reverse(num, rev=0):
    if num == 0:
        return rev

    digit = num % 10

    rev = rev * 10 + digit

    return reverse(num // 10, rev)

num = int(input("Enter number: "))

print("Reverse =", reverse(num))


#Q4) Write a program to find sum of n numbers using recursion.
def sum_numbers(n):
    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

n = int(input("Enter n: "))

print("Sum =", sum_numbers(n))


#Q5) Write a program to find factorial using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input("Enter number: "))

print("Factorial =", factorial(n))


#Q6) Write a program to print Fibonacci series using recursion.
def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")


#Q7) Write a program to find sum of digits using recursion.
def sum_digits(num):
    if num == 0:
        return 0

    return (num % 10) + sum_digits(num // 10)

num = int(input("Enter number: "))

print("Sum of digits =", sum_digits(num))


#Q8) Write a program to check whether a number is prime or not using recursion.
def prime(num, i=2):

    if num <= 1:
        return False

    if i == num:
        return True

    if num % i == 0:
        return False

    return prime(num, i + 1)

num = int(input("Enter number: "))

if prime(num):
    print("Prime Number")
else:
    print("Not Prime Number")


#Q9) Write a program to calculate the m to the power n using recursion.
def power(m, n):

    if n == 0:
        return 1

    return m * power(m, n - 1)

m = int(input("Enter base number: "))
n = int(input("Enter power: "))

print("Result =", power(m, n))


#Q10) Write a program to reverse a number using recursion.
def reverse(num, rev=0):

    if num == 0:
        return rev

    digit = num % 10

    rev = rev * 10 + digit

    return reverse(num // 10, rev)

num = int(input("Enter number: "))

print("Reverse Number =", reverse(num))