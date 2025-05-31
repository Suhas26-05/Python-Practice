# Create a function to find the square of each element in a given list.

def Squ_li(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    return numbers

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"square of each element in a given list is {Squ_li(numbers)}")