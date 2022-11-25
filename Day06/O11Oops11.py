
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'Angular']

    def __str__(self):
        return f"The name is {self.name}\nSalary is {self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val

emp1 = Employee("Nixon",25000)
print(emp1)

print("-" * 40)
print([t for t in emp1])

print("-" * 40)
emp1.append("Python")
print([t for t in emp1])

print("-" * 40)
x = emp1[3]
print(f"x :{x}")

print("-" * 40)
emp1[2] = 'JSP'
print([t for t in emp1])
