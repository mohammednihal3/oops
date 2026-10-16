class Student:
    def __init__(self,mark1,mark2,mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        
    def total(self):
        return self.mark1 + self.mark2 + self.mark3
    
    def average(self):
        return self.total() / 3
    
    def calculate_grade(self):
        average = self.average()
    
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "Fail"
        
mark1 = int(input("Enter marks1 : "))
mark2 = int(input("Enter marks2 : "))
mark3 = int(input("Enter marks3 : "))
    
S1 = Student(mark1, mark2, mark3)
print("Total:", S1.total())
print("Average:", S1.average())
print("Grade:", S1.calculate_grade())