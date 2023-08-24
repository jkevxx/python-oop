class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(f"The student {self.name} is studying")


name = input("Write the student's name: ")
age = input("Write the student's age: ")
grade = input("Write the student's grade: ")
student_1 = Student(name, age, grade)

# student_1.study()

print(f"""
      Student's Data: \n
      Name: {student_1.name} \n
      Age: {student_1.age} \n
      Grade: {student_1.grade} \n
      """)
