"""Variables/attributes associated with the class and are shared by all the instance"""

# Python Object-oriented programming


class Employee:
    raise_percent = 1.45  # class variable

    # constructor
    def __init__(self, fname, lname, pay):
        # instance variables (can be unique for each instance)
        self.first = fname
        self.last = lname
        self.salary = pay
        self.email = fname + "." + lname + "@company.com"

    # method associated with class
    def fullname(self):
        return f"{self.first} {self.last}"

    def update_pay(self):
        self.salary = self.salary * Employee.raise_percent


print(f"{Employee.raise_percent=}")
# object instantiation
emp1 = Employee("Rohit", "Sharma", 300000)
emp2 = Employee("Virat", "Kohli", 250000)

print(f"{Employee.raise_percent=}")
print(f"{emp1.raise_percent=}")
print(f"{emp2.raise_percent=}")

print("=" * 80)

print("Class will update the raise percent:    ")
Employee.raise_percent = 1.35
print(f"{Employee.raise_percent=}")
print(f"{emp1.raise_percent=}")
print(f"{emp2.raise_percent=}")

# print all the properties associated with object
print(f"{emp1.__dict__ }")
print(f"{emp2.__dict__ }")
print(f"{Employee.__dict__ }")

print("=" * 80)

print("emp1 will update the raise percent & it will automatically create an instance variable:  ")
emp1.raise_percent = 1.75
print(f"{Employee.raise_percent=}")
print(f"{emp1.raise_percent=}")
print(f"{emp2.raise_percent=}")

# print all the properties associated with object
print(f"{emp1.__dict__ }")
print(f"{emp2.__dict__ }")
print(f"{Employee.__dict__ }")


