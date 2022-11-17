
emp = {
    'emp1': {'name': 'Micheal', 'age': 34, 'dept': 'finance', 'desig': 'MGR', 'location': 'mumbai'},
    'emp2': {'name': 'Tina', 'age': 32, 'dept': 'HR', 'desig': 'BDM', 'location': 'Pune'},
    'emp3': {'name': 'Kevin', 'age': 29, 'dept': 'Accounts', 'desig': 'Accoutant', 'location': 'mumbai'}
}

print(f"emp :{emp}")

print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print("-" * 40)
print(f"emp2 :{emp['emp2']}")
print("-" * 40)
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
print("-" * 40)

# items = keys + values
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(info[k]))
    print("-" * 40)

print("-" * 40)
# update
emp1 = {'name': 'Micheal', 'age': 34, 'dept': 'finance', 'location': 'mumbai'}
emp2 = {'name': 'Tina', 'age': 32, 'dept': 'HR', 'desig': 'BDM'}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)
emp1.update(emp2)

print(f"emp1 :{emp1}")

print("-" * 40)
emp2 = {'name': 'Tina', 'age': 32, 'dept': 'HR', 'desig': 'BDM'}

print(f"emp2 :{emp2}")

emp2.clear()

print(f"emp2 :{emp2}")

