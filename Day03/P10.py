# Implement a function that takes two lists and returns their union n (all unique elements from both lists)

def union_lists(list1, list2):
    return list(set(list1) | set(list2)) 

if __name__ == "__main__":
    lis1 = list(map(int, input("Enter numbers for List 1: ").split()))
    lis2 = lis = list(map(int, input("Enter numbers for List 2: ").split()))
    print(f"Given Two List Union is {union_lists(lis1, lis2)}")