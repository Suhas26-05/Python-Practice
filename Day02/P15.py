# Given a string, write a function to remove all vowels from it and return the modified string

def remove_vowels(s):
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in s if char not in vowels)

if __name__ == "__main__":
    text = input("Enter a string: ")
    result = remove_vowels(text)
    print(f"String after removing vowels: {result}")
