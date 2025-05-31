# Given a list of numbers, create a function to find the sum of all positive numbers

def sum_of_positive(numbers):
    total = 0
    for i in numbers:
        if i > 0:
            total += i
    return total

if __name__ == "__main__":

    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    su = sum_of_positive(numbers)
    print(f"The sum of All Positive numbers in list is {su}")