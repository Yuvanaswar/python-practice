class Student:
    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept

    def show(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Department: {self.dept}")

students = []

for i in range(2):
    name = input("Enter name: ")
    roll = input("Enter roll no: ")
    dept = input("Enter dept: ")
    s = Student(name, roll, dept)
    students.append(s)

print("\n--- Student Details ---")
for s in students:
    s.show()
    print("-----")
