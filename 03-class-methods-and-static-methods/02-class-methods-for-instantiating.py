"""
    - Class methods are useful, when we don't have anything to do with a specific instance, but to the class itself.
    - The first argument of class method is the `class` itself, typically denoted by `cls`.
    - To make a methods in class, a class method, we use decorator `@classmethod`.
    - Another major use case is, instantiating an instance based on some different logic.
"""


class Employee:
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def full_name(self):
        return self.fname + ' '+self.lname

    def increment_pay(self):
        self.pay *= Employee.raise_amount

    @classmethod
    def change_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        fname, lname, pay = emp_string.split("-")
        return cls(fname, lname, pay)


emp1 = Employee("Rohit", "Sharma", 100)
emp2 = Employee.from_string("virat-kohli-350")

print(emp1.full_name())
print(emp2.full_name())
