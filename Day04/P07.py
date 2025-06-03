# Given two sets, find the union, intersection, and difference between them

def set_operations(set1, set2):
    return set1 | set2, set1 & set2, set1 - set2

if __name__ == "__main__":
    set1 = set(input("Enter first set elements: ").split())
    set2 = set(input("Enter second set elements: ").split())
    union, intersection, difference = set_operations(set1, set2)
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print(f"Difference: {difference}")
