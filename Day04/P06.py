# Write a Python program that counts the number of occurrences of each character in a given string using a dictionary.

def char_count(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count

if __name__ == "__main__":
    string = input("Enter a string: ")
    print(f"Character count: {char_count(string)}")
