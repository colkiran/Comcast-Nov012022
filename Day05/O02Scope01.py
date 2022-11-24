
glbX = 100

def fun(y):                 # y is a local variable
    global glbX
    glbX = 250
    print(f"y :{y}")
    st = "hello world"      # local variable
    print(f"st :{st}")
    print(f"glbX inside :{glbX}")
    # glbX = 250  # local var

print(f"glbX before :{glbX}")

fun(500)

print(f"glbX After :{glbX}")
