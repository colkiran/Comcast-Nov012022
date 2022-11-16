
# emulate c style formatting - printf
format = "Welcome %s, what a %s player"
print(f"format :{format}")
values = ("Sachin", "superb")           # tuple
print(f"values :{values}")
print(format % values)
print("Welcome %s, what a %s player" % ("Sachin", "superb"))

print("-" * 40)
format = "Welcome %s, your rating of %.3f what a %s player"

print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.8, "class"))
print(format % ("Sachin", 4.837821, "class"))
print(format % ("Sachin", 4.8589799, "class"))
print("-" * 40)

print("Welcome %s, your rating of %.3f what a %s player" %  ("Sachin", 4.89799, "class"))

# emulate unis shell syntax
from string import Template

tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
res = tmpl.substitute(name="Sachin", adj="class")
print(res)

# format strings from python
print("Welcome {}, what a {} player for {}".format("Sachin", "Class", "India"))

print("Welcome {0}, what a {1} player for {2}".format("Sachin", "Class", "India"))

print("-" * 40)
print("Welcome {0}, what a {1} player for {2}".format("India","Sachin", "Class"))
print("Welcome {1}, what a {2} player for {2}".format("India","Sachin", "Class"))
print("Welcome {gname}, what a {adj} player for {cntry}".format(cntry = "India",gname = "Sachin", adj="Class"))
c = "India"
g = "Sachin"
a = "Class"

print("Welcome {gname}, what a {adj} player for {cntry}".format(cntry=c, gname = g , adj = a))

print("Welcome {gname} your rating of {rat:.3f} what a {adj} player".format  (gname="Sachin", rat=4.89799, adj="class"))

print("-" * 40)
print("-" * 40)
# interpolation
from math import pi, e
print(f"PI = {pi} and Euler's constant = {e}")

print("PI = {} and Eulers constant = {}".format(pi, e))
print("PI = {} and Eulers constant = {} and magic number = {magic}".format(pi, e, magic=40585))
print("PI = {0} and Eulers constant = {1} and magic number = {magic}".format(pi, e, magic=40585))

print("-" * 40)
full_name = ["Sachin", "Tendulkar"]
print("Mr.{name}".format(name=full_name))
print("Mr.{name[0]} {name[1]}".format(name=full_name))

print("-" * 40)
import math
print(__name__)         # __main__
print(math.__name__)

print("The {mod.__name__} module gives the value of pi = {mod.pi} and eulers constant = {mod.e}".format(mod=math))
