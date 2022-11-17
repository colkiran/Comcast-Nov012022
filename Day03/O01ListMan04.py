"""
sort    => will sort the original list
sorted  => will take a copy of the list and then sort it
"""
# sort
l1 = [8, 4, 1, 7, 9, 3, 5, 2, 10, 6]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending Order  :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending Order :{res_desc}")

print("-" * 40)

l2 = [8, 'zebra', 'apple', 4, 'yellow', 'blue', 1, 'green', 'white', 7, 'maroon', 'pink', 9, 'dog', 'nest', 3, 'cat', 'egg', 5, 2, 10, 6, 1031, 168, 19, 28, 297, 2181]

print(f"l2 :{l2}")

print("-" * 40)

res_asc = sorted(l2, key=ascii)
print(f"Ascending :{res_asc}")

print("-" * 40)

cities = ['bangalore', 'chennai', 'thiruvananthapuram', 'delhi', 'mumbai', 'kanyakumari', 'kolkata', 'vishakapatnam', 'ooty', 'mysore', 'coimbatore']

print(f"cities :{cities}")

print("-" * 40)

print(cities)

print("-" * 40)
res_asc = sorted(cities, key=len)
print(f"Ascending :{res_asc}")

print("-" * 40)
res_desc = sorted(cities, key=len, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 40)
months = ['dec', 'aug', 'apr', 'nov', 'feb', 'oct', 'jan', 'mar', 'may', 'jul', 'jun', 'sep']


print(f"months :{months}")
# sort the dates according to the calendar

print("-" * 40)
from calendar import month_name
print(list(month_name))
l = []
for mth in list(month_name):
    l.append(mth[0:3].lower())

print("-" * 40)

def month_sorted(mon):
  if mon in l:
      return l.index(mon)

res_asc = sorted(months, key=month_sorted)
print(f"Ascending :{res_asc}")

res_desc = sorted(months, key=month_sorted, reverse=True)
print(f"Descending :{res_desc}")