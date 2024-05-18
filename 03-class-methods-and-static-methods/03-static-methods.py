"""
    - Static methods are useful, when a function has nothing to do with any instance, nor with the class itself, but the logic is related to the class and so are grouped together.

    - Like, for an Employee class, if a day is a weekday or not, is neither depended on the individual employee nor on the class itself. But, the function makes sense to be included with the class.

    - For such cases, we use `static methods`. They neither take `instance` nor `class` as a parameter.
    - To mark a function as static, simply use decorator `@staticmethod`.
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
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True


emp1 = Employee("Rohit", "Sharma", 100)
emp2 = Employee.from_string("virat-kohli-350")

print(emp1.full_name())
print(emp2.full_name())

import datetime
my_date = datetime.date(2016,12,8)
print(f"{Employee.is_workday(my_date)=}")
print(f"{emp1.is_workday(my_date)=}")
print(f"{emp2.is_workday(my_date)=}")
