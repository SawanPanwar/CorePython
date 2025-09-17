class Student:
    def get_student(self):
        # Accept student details
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")


class Test(Student):

    def get_marks(self):
        # Accept class and marks
        self.student_class = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.maths = int(input("Maths: "))
        self.physics = int(input("Physics: "))
        self.chemistry = int(input("Chemistry: "))


class Marks(Test):
    # Display student's information along with total marks
    def display(self):
        print("\n\nName:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Class:", self.student_class)
        total_marks = self.maths + self.physics + self.chemistry
        print("Total Marks:", total_marks)


# Create an object of Marks class
m = Marks()

# Collect student details
m.get_student()

# Collect marks details
m.get_marks()

# Display all information
m.display()
