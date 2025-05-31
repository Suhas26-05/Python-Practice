# Write a function that takes two lists and returns their intersection (common elements)

def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

if __name__ == "__main__":
    list1 = input("Enter first list of elements (space-separated): ").split()
    list2 = input("Enter second list of elements (space-separated): ").split()
    
    common_elements = list_intersection(list1, list2)
    print(f"Common elements: {common_elements}")
