# Write a program that checks if a given list is sorted in ascending order

def is_sorted_ascending(lst):
    return lst == sorted(lst)

if __name__ == "__main__":
    lst = input("Enter names separated by spaces: ").split()
    x = is_sorted_ascending(lst)
    if x == True:
        print(f"Give list is sorted in ascending order {lst}")
    else:
        print(f"Give list is not sorted in ascending order {lst}")