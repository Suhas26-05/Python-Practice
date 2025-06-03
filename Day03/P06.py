# Write a Python program to count the occurrences of each element in a given list.
from collections import Counter

def count_occurrences(lst):
    return Counter(lst)


if __name__ == "__main__":
    lis = input("Enter names separated by spaces: ").split()
    print(f"Occurrences of given list is {count_occurrences(lis)}")