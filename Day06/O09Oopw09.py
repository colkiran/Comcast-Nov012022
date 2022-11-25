
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary


emp1 = Employee("Jack", 40000)
print(emp1)

print("-" * 40)
emp2 = Employee("Joe", 35000)
print(emp2)

print("-" * 40)
print(f"add :{emp1 + emp2}")

print("-" * 40)
print(f"sub :{emp1 - emp2}")

print("-" * 40)
print(f"mul :{emp1 * emp2}")

print("-" * 40)
print(f"div :{emp1 / emp2}")

print("-" * 40)
print(f"floor div :{emp1 // emp2}")

