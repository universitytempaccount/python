class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
    def save(self):
        with open("students.txt", "a") as file:
            file.write(self.name + "," + self.roll_no + "\n")

s1 = Student("Ahmad", "101")
s2 = Student("Musa", "102")

s1.display()
s2.display()
s1.save()
s2.save()

print("\nStudent Records:")
with open("students.txt", "r") as file:
    print(file.read())
