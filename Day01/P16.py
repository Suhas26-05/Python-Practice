# Implement a program that prints the multiplication table of a given number

def print_multiplication_table(number):
    print(f"\nMultiplication Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_multiplication_table(num)
