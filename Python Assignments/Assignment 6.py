'''Python Assignment -6 (Patterns)'''
'''Write a program print following patterns:'''


#Question 1
rows = 5

for i in range(rows):
    for j in range(rows):

        # Print star at borders
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


#Question 2
num = 1

for i in range(1, 5):

    for j in range(i):
        print(num, end=" ")
        num = num + 1

    print()


#Question 3
for i in range(1, 5):

    # Spaces
    for s in range(5 - i):
        print(" ", end=" ")

    # Numbers
    num = 1
    for j in range(i):
        print(num, end=" ")

        # Pascal logic
        num = num * (i - j - 1) // (j + 1)

    print()


#Question 4
for i in range(1, 6):

    ch = 65   # ASCII value of A
    for j in range(i):
        print(chr(ch), end=" ")
        ch = ch + 1

    print()


#Question 5
rows = 5
for i in range(rows):

    # Spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")

    # Stars
    for k in range(2 * i + 1):
        print("*", end=" ")

    print()


#Question 6
rows = 5

for i in range(1, rows + 1):

    # Spaces
    for j in range(rows - i):
        print(" ", end=" ")

    # Numbers
    for k in range(1, 2 * i):
        print(k, end=" ")

    print()


#Question 7
rows = 5

for i in range(1, rows + 1):

    # Spaces
    for j in range(rows - i):
        print(" ", end=" ")

    ch = 65

    # Alphabets
    for k in range(2 * i - 1):
        print(chr(ch), end=" ")
        ch = ch + 1

    print()
