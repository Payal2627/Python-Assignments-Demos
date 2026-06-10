class Student:
    def setStudent(self):
        self.sid = int(input("Enter sid : "))
        self.sname = input("Enter sname : ")
        self.percentage = float(input("Enter percentage : "))

    def showStudent(self):
        print("Sid = ",self.sid)
        print("SName = ",self.sname)
        print("Percentage =",self.percentage)

s1 = Student()
s1.setStudent()
s1.showStudent()
