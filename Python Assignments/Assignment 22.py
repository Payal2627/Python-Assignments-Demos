'''Assignment on Pickling and Unpickling'''


#Q1 Create a class Emp (eid,ename,basic)
#Q2
'''
WAP a menu driven program to perform following operations using
files :

a. Add a record
b. Search for a record using id
c. Delete a record using id
d. Edit a record using id.
e. Display all records.
'''

import pickle
import os

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("Employee ID :", self.eid)
        print("Employee Name :", self.ename)
        print("Basic Salary :", self.basic)
        print("----------------------")

filename = "emp.dat"

def add_record():
    f = open(filename, "ab")
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    e = Emp(eid, ename, basic)
    pickle.dump(e, f)

    f.close()
    print("Record Added Successfully")

def display_all():
    try:
        f = open(filename, "rb")

        print("\nEmployee Records")
        print("----------------")
        while True:
            try:
                e = pickle.load(f)
                e.display()
            except EOFError:
                break

        f.close()

    except FileNotFoundError:
        print("File does not exist.")

def search_record():
    eid = int(input("Enter Employee ID to Search: "))

    found = False

    try:
        f = open(filename, "rb")

        while True:
            try:
                e = pickle.load(f)

                if e.eid == eid:
                    print("Record Found")
                    e.display()
                    found = True
                    break

            except EOFError:
                break

        f.close()

        if not found:
            print("Record Not Found")

    except FileNotFoundError:
        print("File does not exist.")

def delete_record():
    eid = int(input("Enter Employee ID to Delete: "))

    found = False

    f1 = open(filename, "rb")
    f2 = open("temp.dat", "wb")

    try:
        while True:
            e = pickle.load(f1)

            if e.eid != eid:
                pickle.dump(e, f2)
            else:
                found = True

    except EOFError:
        pass

    f1.close()
    f2.close()

    os.remove(filename)
    os.rename("temp.dat", filename)

    if found:
        print("Record Deleted Successfully")
    else:
        print("Record Not Found")

def edit_record():
    eid = int(input("Enter Employee ID to Edit: "))

    found = False

    f1 = open(filename, "rb")
    f2 = open("temp.dat", "wb")

    try:
        while True:
            e = pickle.load(f1)

            if e.eid == eid:
                print("Existing Record")
                e.display()

                ename = input("Enter New Name: ")
                basic = float(input("Enter New Salary: "))

                e = Emp(eid, ename, basic)
                found = True

            pickle.dump(e, f2)

    except EOFError:
        pass

    f1.close()
    f2.close()

    os.remove(filename)
    os.rename("temp.dat", filename)

    if found:
        print("Record Updated Successfully")
    else:
        print("Record Not Found")

#main
while True:
    print("\n----- MENU -----")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add_record()

    elif ch == 2:
        search_record()

    elif ch == 3:
        delete_record()

    elif ch == 4:
        edit_record()

    elif ch == 5:
        display_all()

    elif ch == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")