'''Python Assignment 10 (List)'''


#Q1 Python Program to Put Even and Odd elements of a List into two Different Lists
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even List =", even)
print("Odd List =", odd)


#Q2 Python Program to Merge Two Lists and Sort it
list1 = [5, 2, 8, 1]
list2 = [7, 3, 6, 4]

merged = list1 + list2

for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]

print("Sorted List =", merged)


#Q3 Python Program to Sort the List According to the Second Element in Sublist
lst = [[1, 5], [2, 3], [4, 1], [6, 2]]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i][1] > lst[j][1]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted List =", lst)


#Q4 Python Program to Find the Second Largest Number in a List Using Bubble Sort
lst = [12, 45, 8, 30, 22]

for i in range(len(lst)):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Second Largest =", lst[-2])


#Q5 Python Program to Sort a List According to the Length of the Elements within the list.
lst = ["apple", "kiwi", "banana", "grapes", "a"]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if len(lst[i]) > len(lst[j]):
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted List =", lst)


#Q6 Python Program to Find the Union of two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

union = []

for i in list1:
    if i not in union:
        union.append(i)

for i in list2:
    if i not in union:
        union.append(i)

print("Union =", union)


#Q7 Python Program to Find the Intersection of Two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = []

for i in list1:
    if i in list2:
        intersection.append(i)

print("Intersection =", intersection)


#Q8 Print 1 to 100 in snakes and ladder pattern.
num = 1

for row in range(10):
    temp = []

    for col in range(10):
        temp.append(num)
        num += 1

    if row % 2 != 0:
        temp.reverse()

    for x in temp:
        print(x, end="\t")
    print()



#Q9 Write a program to create three lists of numbers, their squares and cubes
numbers = []
squares = []
cubes = []

for i in range(1, 11):
    numbers.append(i)
    squares.append(i * i)
    cubes.append(i * i * i)

print("Numbers =", numbers)
print("Squares =", squares)
print("Cubes =", cubes)


#Q10 Write a program to print list after removing even numbers.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_list = []

for i in lst:
    if i % 2 != 0:
        odd_list.append(i)

print("List after removing even numbers =", odd_list)
