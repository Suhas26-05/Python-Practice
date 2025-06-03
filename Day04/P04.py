# Create a program that checks if two sets have any elements in common.
def have_common_elements(set1, set2):
    return not set1.isdisjoint(set2)

if __name__ == "__main__":
    set1 = set(input("Enter first set elements separated by space: ").split())
    set2 = set(input("Enter second set elements: ").split())
    print(f"Sets have common elements: {have_common_elements(set1, set2)}")
