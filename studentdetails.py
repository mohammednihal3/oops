class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
s1 = Student("Anu", 20, "computer Science")
s2 = Student("Abhinand",22,"cs")

print("student name: ",s1.name)
print("student age: ",s1.age)
print("student course: ",s1.course)
print("student name: ",s2.name)
print("student age: ",s2.age)
print("student course: ",s2.course)