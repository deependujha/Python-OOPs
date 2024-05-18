"""Variables/attributes associated with the class and are shared by all the instance"""
# Python Object-oriented programming


class Employee:
    employee_count = 0 # class variable
    # constructor
    def __init__(self, fname, lname, pay):
        # instance variables (can be unique for each instance)
        self.first = fname
        self.last = lname
        self.salary = pay
        self.email = fname + "." + lname + "@company.com"
        Employee.employee_count +=1

    # method associated with class
    def fullname(self):
        return f"{self.first} {self.last}"

print(f"{Employee.employee_count=}")
# object instantiation
emp1 = Employee("Rohit", "Sharma", 300000)
emp2 = Employee("Virat", "Kohli", 250000)

print(f"{Employee.employee_count=}")
print(f"{emp1.employee_count=}")
print(f"{emp2.employee_count=}")

print("="*80)

# print all the properties associated with object
print(f"{emp1.__dict__ }")
print(f"{emp2.__dict__ }")
print(f"{Employee.__dict__ }")


