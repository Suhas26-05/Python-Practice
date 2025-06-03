# Implement a function that takes a list of strings and returns a set of unique characters present in all strings.


def common_characters(strings):
    return set.intersection(*(set(s) for s in strings))

if __name__ == "__main__":
    strings = input("Enter strings separated by space: ").split()
    print(f"Common characters in all strings: {common_characters(strings)}")
