# Given a list of words, count the number of words with more than five characters.

def count_long_words(words):
    count = 0
    for word in words:
        if len(word) > 5:
            count += 1
    return count

if __name__ == "__main__":
    words = input("Enter words separated by spaces: ").split()
    result = count_long_words(words)
    print(f"Number of words with more than five characters: {result}")
