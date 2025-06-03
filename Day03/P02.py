#  Write a program that finds the largest and smallest elements in a list

def max_min(lis):
    return max(lis), min(lis)

if __name__ == "__main__":
    lis = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"largest and smallest elements in a list is {max_min(lis)}")