# Given a list of names, remove all duplicate names and print the unique names.
def remove_duplicates(names):
    unique_names = list(set(names))
    return unique_names

if __name__ == "__main__":
    lis = input("Enter names separated by spaces: ").split()
    print(f"After Duplicates removed list is {remove_duplicates(lis)}")