data = []
print()

data = list()
print()

data = [1,2,3,4]
print(data)
data = list([1,2,3,4])
print(data)

data = [1,2,3,4,5]
#If we specify element which is not present then error is raised
index = data.index(30)
print(index)

data = [1,2,3,4,5]
x = data.pop()
print(data)
print(x,"  was removed")
data.remove(2) #Removes element which is specified
print(data)
#If element is not present then error is raised
# data.remove(20) #Removes element which is specified
# print(data)
#removes element with specified index
del data[0]
print(data)
data.clear()
print(data)

data = [1,2,4,1,33,2,1,4,55,46,1,2,4,55,7,8,10]
#How many elements are there in list
print(len(data))
#Calculate sum of all elements
print(sum(data))
#Find maximum element
print(max(data))
#Find minimum element
print(min(data))
data.sort()
print(data)
data.sort(reverse=True)
print(data)
data.reverse()
print(data)
print(data.count(1)) #It will tell how many times 1 is present in list

data = [1,2,3,4,5]
#Modify the element using index
data[0] = 44
print(data)

data = [1,2,3,4,5]
print(data)
print(data[3])
print(data[-1])
for x in data:
    print(x)

data = [1,2,3,4,5]
data.append(55)
print(data)
data.insert(1,90)
print(data)
#If index is invalid, it adds element towards the end of list
data.insert(100,90)
print(data)
extra = [11,22,33]
data.extend(extra)
print(data)