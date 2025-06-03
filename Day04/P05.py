# Given a list of dictionaries, find the dictionary with the highest value for a specific key

def highest_value_dict(dicts, key):
    return max(dicts, key=lambda x: x.get(key, float('-inf')))

if __name__ == "__main__":
    dicts = eval(input("Enter list of dictionaries: "))
    key = input("Enter key to compare: ")
    print(f"Dictionary with highest '{key}': {highest_value_dict(dicts, key)}")
