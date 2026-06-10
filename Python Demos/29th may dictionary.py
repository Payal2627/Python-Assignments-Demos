data = {}
print(data)
#This tells the data type 
print(type(data))
data = dict()
print(data)
#This tells the data type 
print(type(data))

data = {101:"Priyanka",102:"Ritu",103:"Zunaid",104:"Shruti"}
print(data)
print(data.keys())
print(data.values())
print(data.items())
print("------------------------------")
#It will fetch only keys
for x in data:
    print(x)
print("------------------------------")
for x in data.keys():
    print(x)
print("------------------------------")
for x in data.values():
    print(x)
print("------------------------------")
for x in data.items():
    print(x)
print("------------------------------")
for x,y in data.items():
    print(x," = ",y)


data = {101:"Priyanka",102:"Ritu",103:"Zunaid",104:"Shruti"}
print("Before removing : ",data)
#It removes the last item
item = data.popitem()
print(item)
print("After removing :",data)
#If key is not present it will raise error
item = data.pop(101)
print(item)
print("After removing :",data)
#If key is not present it will raise error
del data[106] #Remove using key
print(data)
data.clear()#Removes all items
del data #Remove items as well as dictionary object

data = [10,20,30,40,45]
# in -> membership operator
if 30 in data:
    print(30, " is present")
else:
    print(30," is not present")

data = {101:"Priyanka",102:"Ritu",103:"Zunaid",104:"Shruti"}
if 103 in data:
    print(103," is present")
#It will return the value of that key
#If key does not exist then error is returned
x = data[101]
print(x)
#If key does not exist, it will return None, instead of error
value = data.get(111)
print(value)
#We can specify customized output if value not found
value = data.get(111,"Not found")
print(value)
print(len(data))
print(max(data))
print(min(data))

data = {101:"Priyanka",102:"Ritu",103:"Zunaid",104:"Shruti"}
#To add new item
data[105] = "Kiran"
print(data)
#To modify the item
data[101] = "Seema"
print(data)
mydict = {1:"A",2:"B",3:"C"}
#Update is used to add new dict into existing dict
data.update(mydict)
print(data)