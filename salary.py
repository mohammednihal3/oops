class Employee:
    def __init__(self, name, salary, incriment):
        self.name = name
        self.salary = salary
        self.incriment = incriment
    
    def calculate_salary(self):
        updated_salary = self.salary + self.salary * self.incriment / 100
        return updated_salary
    
name = input("Enter Employee Name : ")
salary = float(input("Enter current salary : "))
incriment = float(input("Enter incriment percentage : "))

E1 = Employee(name, salary, incriment)
E1.calculate_salary()
print("Updated salary : ",E1.calculate_salary())