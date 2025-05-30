# Swap the values of two variables using a program

def swap_of_val(a,b):
    return b, a

if __name__ == "__main__":
    a = int(input("Enter 1st Value: "))
    b = int(input("Enter 2nd Value: "))
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = swap_of_val(a,b)
    print(f"After Swapping: a = {a}, b = {b}")