# Given two dictionaries, merge them into a single dictionary.
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

if __name__ == "__main__":
    dict1 = eval(input("Enter first dictionary (e.g., {'a':1, 'b':2}): "))
    dict2 = eval(input("Enter second dictionary: "))
    print(f"Merged Dictionary is {merge_dicts(dict1, dict2)}")