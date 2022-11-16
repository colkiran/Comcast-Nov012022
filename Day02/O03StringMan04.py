
# conversions
print("Conversions".center(40, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("-" * 40)
print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))

print("-" * 40)
print("{num:15} Tendulkar".format(num="Sachin"))
print("{num:15} Tendulkar".format(num=30))
print("{num:3} Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 40)
print("{:10.2f}".format(pi))
print("{:010.2f}".format(pi))

print("{:15}".format("Sachin"))
print("{:>15}".format("Sachin"))
print("{:^15}".format("Sachin"))
print("{:<15}".format("Sachin"))

print("-" * 40)
print("{:*>15}".format("Sachin"))
print("{:*^15}".format("Sachin"))
print("{:*<15}".format("Sachin"))

print("-" * 40)
print("{:-^40}".format("hello world"))
print("hello world".center(40, "-"))
