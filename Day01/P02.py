# Check if a number is even or odd.

def EorO(n):
    if n % 2 == 0:
        print(f"Given number or {n} is even")
    else:
        print(f"Given number or {n} is odd")

if __name__ == "__main__":
    n = int(input("Enter a Number:"))
    EorO(n)