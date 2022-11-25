
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name}\nSalary is {self.salary}"

    # This will work for != also
    def __eq__(self, other):
        return self.salary == other.salary

    # works for less than
    def __gt__(self, other):
        return self.salary > other.salary



emp1 = Employee("Robin", 40000)
print(emp1)

print("-" * 40)

emp2 = Employee("Kevin", 45000)
print(emp2)

print("-" * 40)

if emp1 == emp2:
    print("{} salary of {} is  equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)

if emp1 > emp2:
    print("{} salary of {} is greater than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is less than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)

print(emp1 >= emp2)