# Write a Python program to check if a given number is a prime number.

def Prime_number(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    x = Prime_number(num)

    if x > 2:
        print(f"Given number {num} is not Prime number")
    else:
        print(f"Given number {num} is Prime number")