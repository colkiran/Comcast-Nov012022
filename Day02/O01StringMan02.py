
st1 = "the quick brown fox jumps over the lazy dog"
st2 = "hello world"

print("find".center(40,"-"))
print(f'st1 :{st1}')

pos = st1.find("the")
print(f"position :{pos}")

pos = st1.find("the", st1.find("the") + 1)
print(f"position :{pos}")

print("replace".center(40,"-"))
print(f"st1 :{st1}")

res1 = st1.replace("the", "The")
print(f"res1 :{res1}")

res2 = st1.replace("the", "The", 1)
print(f"res1 :{res2}")

print(f"st2 :{st2}")
res3 = st2.replace("l", "L")
print(f"res3 :{res3}")

print("-" * 40)
# maketrans and transalte
print(f"st2 :{st2}")
a = 'helowrd'
b = 'HELOWRD'                   # length of a and b should be the same
resTbl = st2.maketrans(a, b)
print(resTbl)

print("-" * 40)
print(ord("h"), "\t", ord("H"))
print(ord("e"), "\t", ord("E"))
print(ord("l"), "\t", ord("L"))

print("-" * 40)
res = st2.translate(resTbl)
print(f"res :{res}")

print("-" * 40)
st = "*******hello********"
print(f"st :{st}")

res = st.rstrip("*")
print(f"res :{res}")

res1 = res.lstrip("*")
print(f"res1 :{res1}")

res2 = st.strip("*")
print(f'res2 :{res2}')

