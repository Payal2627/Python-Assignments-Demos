'''Python Assignment 4 (Looping)'''

#Question 1) WAP to print all even numbers until n.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)


#Question 2) WAP to print all odd numbers until n.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)


#Question 3) WAP to print sum of series upto n.
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)


#Question 4) WAP to print factorial of a number .
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


#Question 5) WAP to print Fibonacci series upto n.
n = int(input("Enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a)

    c = a + b
    a = b
    b = c


#Question 6) WAP to check if a given number is prime number or not.
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")


#Question 7) WAP to print all integers upto n that aren’t divisible by 2 and 3.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        print(i)


#Question 8) WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)


#Question 9) WAP to print all numbers in a range divisible by a given number.
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
n = int(input("Enter divisor: "))

for i in range(start, end + 1):
    if i % n == 0:
        print(i)


#Question 10) WAP to check if given number is Perfect Number.
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")


#Question 11) WAP to check if given number Strong Number.
n = int(input("Enter a number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    n = n // 10

if sum == temp:
    print("Strong Number")
else:
    print("Not Strong Number")


#Question 12) Write a program to check if given number is Armstrong number or not.
n = int(input("Enter a number: "))
temp = n
digits = len(str(n))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + (digit ** digits)
    n = n // 10

if sum == temp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")