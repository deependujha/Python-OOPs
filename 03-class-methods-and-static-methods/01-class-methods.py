"""
    - Class methods are useful, when we don't have anything to do with a specific instance, but to the class itself.
    - The first argument of class method is the `class` itself, typically denoted by `cls`.
    - To make a methods in class, a class method, we use decorator `@classmethod`.
"""

class Employee:
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def increment_pay(self):
        self.pay *= Employee.raise_amount


    @classmethod
    def change_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee("Rohit", "Sharma", 100)
emp2 = Employee("Virat", "Kohli", 200)

print(f"{Employee.raise_amount=}")
print(f"{emp1.raise_amount=}")
print(f"{emp2.raise_amount=}")

print("="*80)

print("calling class method by classname")
Employee.change_raise_amount(1.07)

print(f"{Employee.raise_amount=}")
print(f"{emp1.raise_amount=}")
print(f"{emp2.raise_amount=}")

print("="*80)

print("calling class method by instance. This will also change it for all the instances of the class. But, not typically used.")
emp1.change_raise_amount(1.35)

print(f"{Employee.raise_amount=}")
print(f"{emp1.raise_amount=}")
print(f"{emp2.raise_amount=}")
