# Create a loop that prints all prime numbers between 1 and N.

def Prime_number(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter the value of N: "))
    print(f"Prime numbers between 1 and {n} are:")

    for num in range(2, n + 1):
        divisor_count = Prime_number(num)
        if divisor_count == 2:
            print(num, end=' ')
