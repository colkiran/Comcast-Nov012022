

class Employee:

    def __init__(self, name):
        self.__name = name              # private variable
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'Angular']

    def __str__(self):
        return self.__name + " - " + ", ".join([v for v in self.tech])

emp1 = Employee("Ruben")
print(emp1)

print("-" * 40)
print(emp1.__dict__)
emp1._Employee__name = "Peter"
print(emp1)
print(emp1.__dict__)

