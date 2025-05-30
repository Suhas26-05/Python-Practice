# Calculate the sum of digits of a given number.

def sum_of_digits(numbers):
    total = 0
    while numbers > 0:
        total += numbers % 10
        numbers = numbers // 10
    return total

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    number = abs(number)
    res = sum_of_digits(number)

    print(f"Sum of digits: {res}")