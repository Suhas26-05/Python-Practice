# Write a Python program to find the length of the longest word in a sentence

def longest_word_length(sentence):
    words = sentence.split()
    if not words:
        return 0  
    return max(len(word) for word in words)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    length = longest_word_length(sentence)
    print(f"Length of the longest word: {length}")

