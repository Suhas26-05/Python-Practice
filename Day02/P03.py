# Implement a function that returns the factorial of a given number using recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
if __name__ == "__main__":
    n = int(input("Enter a Number: "))
    fact = factorial(n)
    print(f"For Given Number {n} Factorial is {fact}")
