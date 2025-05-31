# Create a function that takes a list of strings and returns the list sorted alphabetically.

def Sort_Alpha(string):
    return sorted(string)

if __name__ == "__main__":
    strings = input("Enter strings separated by spaces: ").split()
    sorted_list = Sort_Alpha(strings)
    print(f"Sorted list: {sorted_list}")