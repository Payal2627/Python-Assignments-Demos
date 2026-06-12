class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_result(self):

        total = (self.sy_marks.computer +
                 self.ty_marks.theory +
                 self.ty_marks.practical)

        average = total / 3

        if average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("\n----- STUDENT RESULT -----")
        print("Roll Number :", self.roll_no)
        print("Name        :", self.name)
        print("Total Marks :", total)
        print("Average     :", average)
        print("Grade       :", grade)