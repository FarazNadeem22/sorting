import time

class Student:
    count = 0
    def __init__(self, name, roll_no, marks, grade):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = grade
        Student.count += 1

    def display(self):
        print("Name: ", self.name)
        print("Roll Number: ", self.roll_no)
        print("Marks: ", self.marks)

    def __str__(self):
        """
        Do not print here otherwise you will get an additional None. So this cannot be a void function it will always
        return something. If you do not manually return something it will automatically return None
        """
        return ("Name: " + self.name + ", Roll Number: " + str(self.roll_no) + ", Marks Obtained: " + str(self.marks)
                + ", Grade: " + self.grade)

    def __del__(self):
        """
        This is a destructor like a constructor. This is just here for academic reasons. To invoke the destructor all you
        need to do it set the object = None. It turns out that the destructor is always invoked before the program ends.
        """
        print("Destructor Invoked")

    def getMarks(self):
        return self.marks

    @classmethod
    def objectCount(cls):
        print("Total number of students: ", cls.count)

def get_grade(marks):
    if marks > 92:
        return "A+"
    elif marks > 90:
        return "A-"
    elif marks > 87:
        return "B+"
    elif marks > 85:
        return "B"
    elif marks > 80:
        return "B-"
    elif marks > 70:
        return "C"
    elif marks > 59:
        return "D"
    else:
        return "F"


no_students = int(input("Enter Number od Students: "))
student_lst = []

for x in range(no_students):
    roll_no = x + 1
    print("Roll Number Issued: ", roll_no)
    name = input("What is your name: ")


    while(True):
        marks_obtained = int(input("What marks did you obtain: "))
        if marks_obtained < 0 or marks_obtained > 100:
            print("Marks obtained must be between 0 and 100, try again")
            time.sleep(1)
        else:
            break

    grade = get_grade(marks_obtained)
    student_x = Student(name,roll_no, marks_obtained, grade)
    student_lst.append(student_x)

# https://www.programiz.com/python-programming/methods/list/sort
# https://www.w3schools.com/python/ref_list_sort.asp
student_lst.sort(key=lambda student: student.marks, reverse=True)

for students in student_lst:
    print(students.__str__())

print("Number of Students: ", Student.objectCount())