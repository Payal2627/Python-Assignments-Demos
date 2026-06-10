'''Python Assignment -7 (Patterns)'''

#Question 1) Write a program print following patterns:
n = 4

for i in range(1, n + 1):
    
    for j in range(n - i):
        print("  ", end="")

    print("*", end="")

    
    if i > 1:
        for j in range(2 * i - 3):
            print("  ", end="")
        print("*", end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print("  ", end="")

    print("*", end="")

    if i > 1:
        for j in range(2 * i - 3):
            print("  ", end="")
        print("*", end="")

    print()


#Question 2
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


#Question 3
n = 5

for i in range(1, n + 1):

    for j in range(1, i + 1):

        if i == n or j == 1 or j == i:
            print(j, end=" ")
        else:
            print(" ", end=" ")

    print()


#Question 4
n = 5

for i in range(1, n + 1):

    
    for j in range(n - i):
        print(" ", end=" ")

    
    for j in range(i, 2 * i):
        print(j, end=" ")

    
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")

    print()


#Question 5
n = 5

for i in range(1, n + 1):

    
    for j in range(n - i):
        print("  ", end="")

    for j in range(1, i + 1):

        if i == n or j == 1 or j == i:
            print(j, end=" ")
        else:
            print("  ", end="")

    print()


#Question 6
n = 5

for i in range(1, n + 1):

    for j in range(1, n + 1):

        if j == i or j == n or i == 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")

    print()


#Question 7
n = 5

for i in range(1, n + 1):

    
    for j in range(n - i):
        print(" ", end=" ")

    
    for j in range(1, i + 1):
        print(j, end=" ")

    
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()


#Question 8
n = 5

for i in range(1, n + 1):

   
    for j in range(1, i + 1):
        print(j, end=" ")

    
    for j in range(2 * (n - i)):
        print(" ", end=" ")

    
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()