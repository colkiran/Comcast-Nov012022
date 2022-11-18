
# immutable dictionary
from collections import namedtuple

nmdTpl = namedtuple("Product", "prodid pname price category")
prod = nmdTpl(prodid="PR101", pname="Dairy Milk", price=180, category="Choclate")

print(f"prod :{prod}")

print("\n","-" * 40)
print(f"Product ID   :{prod.prodid}")
print(f"Product Name :{prod.pname}")
print(f"Price        :{prod.price}")
print(f"Category     :{prod.category}")

# prod.pname = "Kit Kat"
