# Create a function that takes a list of strings and returns the list sorted by the length of the strings.

def sort_by_length(strings):
    return sorted(strings, key=len)

if __name__ == "__main__":
    string = input("Enter names separated by spaces: ").split()

    print(f"After Sorted Strings {sort_by_length(string)}")
