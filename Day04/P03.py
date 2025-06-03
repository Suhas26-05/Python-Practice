# Implement a function that removes a key-value pair from a dictionary
def remove_key(d, key):
    d.pop(key, None)
    return d

if __name__ == "__main__":
    d = eval(input("Enter a dictionary: "))
    key = input("Enter key to remove: ")
    print(f"Updated Dictionary: {remove_key(d, key)}")
