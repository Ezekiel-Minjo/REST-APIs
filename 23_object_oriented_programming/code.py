class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades
                                      )
    
    def __str__(self):
        return f"{self.name}"

student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Rolf", (90, 90, 93, 78, 90))
# print(student, student2)
print(f"{student}, avarage is: {student.average()}")
print(f"{student2}, avarage is: {student2.average()}")

# print(student.average(), student2.average())
