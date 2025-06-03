# Write a program that finds the most frequent element in a list

from collections import Counter

def most_frequent(lst):
    return Counter(lst).most_common(1)[0]

if __name__ == "__main__":
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    element, freq = most_frequent(lst)
    print(f"Most frequent element is {element} with frequency {freq}")
