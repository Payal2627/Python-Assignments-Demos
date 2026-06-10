'''Python Assignment on set'''


#Q1 Write a Python program to find elements in a given set that are not in another set.
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 60}

result = s1 - s2

print("Elements in first set but not in second set:")
print(result)


#Q2 Write a Python program to remove the intersection of a second set with a first set.
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 60}

s1 = s1 - (s1 & s2)

print("First set after removing common elements:")
print(s1)


#Q3 Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
strings = ["apple banana", "banana orange", "apple mango"]

words = []

for s in strings:
    temp = s.split()
    for word in temp:
        words.append(word)

unique_words = set(words)

for word in unique_words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(word, ":", count)


#Q4 Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
lst = [1, 5, 7, -1, 5]
target = 6

print("Pairs are:")

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])


#Q5 Write a Python program to find the longest common prefix of all strings. Use the Python set.
strings = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(strings[0])):
    chars = set()

    for word in strings:
        if i < len(word):
            chars.add(word[i])
        else:
            chars.add("")

    if len(chars) == 1:
        prefix += strings[0][i]
    else:
        break

print("Longest Common Prefix:", prefix)


#Q6 Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.
nums = [1, 4, 3, 6, 7, 0]

max_product = nums[0] * nums[1]
num1 = nums[0]
num2 = nums[1]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        product = nums[i] * nums[j]

        if product > max_product:
            max_product = product
            num1 = nums[i]
            num2 = nums[j]

print("Numbers:", num1, num2)
print("Maximum Product:", max_product)


#Q7 Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Missing in second set:", missing_in_set2)
print("Missing in first set:", missing_in_set1)


#Q8 Write a Python program to find all the anagrams and group them together from a given list of strings.
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print("Anagram Groups:")

for value in groups.values():
    print(value)


#Q9 Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
nums = [1, 2, 3, 4, 5, 6]
target = 10

result = set()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == target:
                result.add((nums[i], nums[j], nums[k]))

print("Combinations:")

for item in result:
    print(item)
