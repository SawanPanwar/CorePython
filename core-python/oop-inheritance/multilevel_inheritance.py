class Student:
    def getStudent(self):
        # Accept student details
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")


class Test(Student):

    def getMarks(self):
        # Accept class and marks
        self.studentClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        self.physics = int(input("Physics: "))


class Marks(Test):
    # Display student's information along with total marks
    def display(self):
        print("\n\nName:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Class:", self.studentClass)
        total_marks = self.literature + self.math + self.biology + self.physics
        print("Total Marks:", total_marks)


# Create an object of Marks class
m = Marks()

# Collect student details
m.getStudent()

# Collect marks details
m.getMarks()

# Display all information
m.display()
