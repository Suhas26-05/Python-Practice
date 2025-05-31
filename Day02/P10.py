# Create a function that takes a number as input and prints its multiplication table

def print_multiplication_table(number):
    print(f"\nMultiplication Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_multiplication_table(num)
