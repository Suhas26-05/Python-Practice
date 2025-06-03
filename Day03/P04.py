# Create a program that finds the common elements between two lists and stores them in a new list.

def comm_lis(lis1, lis2):
    return list(set(list1) & set(list2))

if __name__ == "__main__":
    list1 = input("Enter first list of elements (space-separated): ").split()
    list2 = input("Enter second list of elements (space-separated): ").split()
    
    common_elements = comm_lis(list1, list2)
    print(f"Common elements: {common_elements}")
