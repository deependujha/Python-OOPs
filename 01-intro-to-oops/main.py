# Python Object-oriented programming

class Employee:
    
    # constructor
    def __init__(self, fname, lname, pay):
        # instance variables (can be unique for each instance)
        self.first = fname
        self.last = lname
        self.salary = pay
        self.email = fname + '.' + lname +'@company.com'

    # method associated with class
    def fullname(self):
        return f'{self.first} {self.last}'


# object instantiation
emp1 = Employee('Rohit', 'Sharma', 300000)
emp2 = Employee('Virat', 'Kohli', 250000)



# both are similar, first one gets converted to second
print(emp1.fullname())
print(Employee.fullname(emp2))