# Write a function to remove all duplicate characters from a given string

def dup_char(chars):
    seen = set()
    result = []
    for char in chars:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    chars = input("Enter a sentence: ")
    print(f"After Removing duplicates in give string {dup_char(chars)}")