# Given a list of words, concatenate them into a single string separated by spaces.

def concatenate_words(words):
    return ' '.join(words)

if __name__ == "__main__":
    words = input("Enter words separated by spaces: ").split()
    result = concatenate_words(words)
    print(f"Concatenated string: '{result}'")
