# Given a list of integers, find all the even numbers and store them in a new list

def even_nums(numbers):
    even = []

    for i in numbers:
        if i % 2 == 0:
            even.append(i)

    return even

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    e = even_nums(numbers)

    print("Even numbers from List is/are ", e)