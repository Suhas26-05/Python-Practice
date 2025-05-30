# Calculate the area of a rectangle given its length and width.

def aor(a,b):
    return a*b

if __name__ == "__main__":
    a = int(input("Enter Length of Rectangle: "))
    b = int(input("Enter Width of Rectangle: "))
    print("Area of Rectangle is",aor(a,b))