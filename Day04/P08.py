# Create a function that takes a list of dictionaries and sorts them based on a specified key.

def sort_dicts(dicts, sort_key):
    return sorted(dicts, key=lambda x: x.get(sort_key, 0))

if __name__ == "__main__":
    dicts = eval(input("Enter a list of dictionaries: "))
    key = input("Enter key to sort by: ")
    print(f"Sorted list: {sort_dicts(dicts, key)}")
