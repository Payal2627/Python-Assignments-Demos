'''Python Assignment Inheritence'''

'''
Create a class Student with following
a. data members :
i. StudentId
ii. Name
iii. Age
iv. Percentage
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. Method CalculateRank
v. Override __str__ Method
'''

class Student:

    def __init__(self, studentId=0, name="", age=0, percentage=0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.studentId = int(input("Enter Student ID : "))
        self.name = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.percentage = float(input("Enter Percentage : "))

    def display(self):
        print("Student ID :", self.studentId)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Percentage :", self.percentage)

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        else:
            return "Pass"

    def __str__(self):
        return f"ID={self.studentId}, Name={self.name}, Age={self.age}, Percentage={self.percentage}"



'''
Create a derived class from Student as EnggStudent with :
a. Data members as :
i. Branch
ii. InternalMarks
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. override Method CalculateRank
v. Override __str__ Method
'''
class EnggStudent(Student):

    def __init__(self, studentId=0, name="", age=0,
                 percentage=0, branch="", internalMarks=0):

        super().__init__(studentId, name, age, percentage)

        self.branch = branch
        self.internalMarks = internalMarks

    def accept(self):
        super().accept()

        self.branch = input("Enter Branch : ")
        self.internalMarks = float(input("Enter Internal Marks : "))

    def display(self):
        super().display()

        print("Branch :", self.branch)
        print("Internal Marks :", self.internalMarks)

    def calculateRank(self):
        total = self.percentage + (self.internalMarks / 10)

        if total >= 80:
            return "Excellent"
        elif total >= 60:
            return "Good"
        else:
            return "Average"

    def __str__(self):
        return super().__str__() + \
               f", Branch={self.branch}, InternalMarks={self.internalMarks}"


'''
Create a class MedicalStudent inherited from Student with following:
i. Data members :Specialization
ii. MarksOfInternship
b. Add the following methods :
i. Parameterized constructor
ii. Display
iii. Accept
iv. override Method CalculateRank
v. Override __str__ Method
'''
class MedicalStudent(Student):

    def __init__(self, studentId=0, name="", age=0,
                 percentage=0, specialization="", internshipMarks=0):

        super().__init__(studentId, name, age, percentage)

        self.specialization = specialization
        self.internshipMarks = internshipMarks

    def accept(self):
        super().accept()

        self.specialization = input("Enter Specialization : ")
        self.internshipMarks = float(input("Enter Internship Marks : "))

    def display(self):
        super().display()

        print("Specialization :", self.specialization)
        print("Internship Marks :", self.internshipMarks)

    def calculateRank(self):
        total = self.percentage + (self.internshipMarks / 10)

        if total >= 85:
            return "Outstanding"
        elif total >= 65:
            return "Very Good"
        else:
            return "Good"

    def __str__(self):
        return super().__str__() + \
               f", Specialization={self.specialization}, InternshipMarks={self.internshipMarks}"



'''
Create a class College which has collection of students. Add the
following methods :
a. Parameteried constructor for number of students.
b. AddStudent
c. GetStudent
d. RemoveStudent
e. Override __str__ Method
'''
class College:

    def __init__(self, size):
        self.size = size
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.size:
            self.students.append(student)
            print("Student Added Successfully")
        else:
            print("College is Full")

    def getStudent(self, studentId):
        for s in self.students:
            if s.studentId == studentId:
                return s

        return None

    def removeStudent(self, studentId):
        for s in self.students:
            if s.studentId == studentId:
                self.students.remove(s)
                print("Student Removed")
                return

        print("Student Not Found")

    def __str__(self):
        result = "\n----- Student List -----\n"

        for s in self.students:
            result += str(s) + "\n"

        return result


# Main Program

college = College(5)

while True:

    print("\n1. Add Engineering Student")
    print("2. Add Medical Student")
    print("3. Display All Students")
    print("4. Search Student")
    print("5. Remove Student")
    print("6. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        s = EnggStudent()
        s.accept()
        college.addStudent(s)

    elif choice == 2:
        s = MedicalStudent()
        s.accept()
        college.addStudent(s)

    elif choice == 3:
        print(college)

    elif choice == 4:
        sid = int(input("Enter Student ID : "))

        student = college.getStudent(sid)

        if student:
            student.display()
            print("Rank :", student.calculateRank())
        else:
            print("Student Not Found")

    elif choice == 5:
        sid = int(input("Enter Student ID : "))
        college.removeStudent(sid)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")