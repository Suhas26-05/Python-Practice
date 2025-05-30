# Write a program that calculates the factorial of a given number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {num} is: {factorial(num)}")
