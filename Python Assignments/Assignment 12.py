'''Python Assignment 12 (List)'''


#Q1 Python Program to Replace all Occurrences of ‘a’ with $ in a String
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch == 'a':
        result += '$'
    else:
        result += ch

print("New String:", result)


#Q2 Python Program to Remove the nth Index Character from a Non-Empty String
s = input("Enter a string: ")
n = int(input("Enter index to remove: "))

result = ""

for i in range(len(s)):
    if i != n:
        result += s[i]

print("String after removal:", result)


#Q3 Python Program to Detect if Two Strings are Anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


#Q4 Python Program to Form a New String where the First Character and the Last Character have been Exchanged
s = input("Enter a string: ")

if len(s) > 1:
    s = s[-1] + s[1:-1] + s[0]

print("New String:", s)


#Q5 Python Program to Count the Number of Vowels in a String
s = input("Enter a string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)


#Q6 Python Program to Take in a String and Replace Every Blank Space with Hyphen
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == " ":
        result += "-"
    else:
        result += ch

print("New String:", result)


#Q7 Python Program to Calculate the Length of a String Without Using a Library Function
s = input("Enter a string: ")

count = 0

for ch in s:
    count += 1

print("Length of string:", count)


#Q8 Python Program to Remove the Characters of Odd Index Values in a String
s = input("Enter a string: ")

result = ""

for i in range(len(s)):
    if i % 2 == 0:
        result += s[i]

print("Result:", result)


#Q9 Python Program to Calculate the Number of Words and the Number of Characters Present in a String
s = input("Enter a string: ")

words = 1
chars = 0

for ch in s:
    chars += 1
    if ch == " ":
        words += 1

print("Number of words:", words)
print("Number of characters:", chars)


#Q10 Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

len1 = 0
len2 = 0

for ch in s1:
    len1 += 1

for ch in s2:
    len2 += 1

if len1 > len2:
    print("Larger String:", s1)
elif len2 > len1:
    print("Larger String:", s2)
else:
    print("Both strings are equal in length")


#Q11 Python Program to replace every blank space with hyphen in a string.
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == " ":
        result += "-"
    else:
        result += ch

print("Result:", result)


#Q12 Python Program to count number of lowercase characters in a string.
s = input("Enter a string: ")
count = 0

for ch in s:
    if ch >= 'a' and ch <= 'z':
        count += 1

print("Lowercase characters:", count)


#Q13 Python Program to count number of digits and letters in a string.
s = input("Enter a string: ")

digits = 0
letters = 0

for ch in s:
    if ch >= '0' and ch <= '9':
        digits += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letters += 1

print("Letters:", letters)
print("Digits:", digits)


#Q14 Python Program to count the occurrences of ach word in a string.
s = input("Enter a string: ")

words = s.split()

for i in range(len(words)):
    count = 1

    for j in range(i):
        if words[i] == words[j]:
            count = 0
            break

    if count != 0:
        count = 0
        for k in range(len(words)):
            if words[i] == words[k]:
                count += 1

        print(words[i], "=", count)


#Q15 Python Program to find larger string without using built-in functions.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

c1 = 0
c2 = 0

for ch in s1:
    c1 += 1

for ch in s2:
    c2 += 1

if c1 > c2:
    print("Larger String:", s1)
elif c2 > c1:
    print("Larger String:", s2)
else:
    print("Both strings have same length")