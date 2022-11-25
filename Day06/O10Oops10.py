
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'Angular']

    def __str__(self):
        return f"The name is {self.name}\nSalary is {self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)


emp1 = Employee("Ricard", 64500)
print(emp1)

print("-" * 40)
print([t for t in emp1])

print("-" * 40)
print(len(emp1))