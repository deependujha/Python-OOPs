"""
    dunder: double underscore method
"""


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        "Unambiguous representation of the class. Meant to be used by developers for debugging"
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        "to be used by consumers for knowing what it is"
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        "overriding addition on the class objects"
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)

print(len(emp_1))
