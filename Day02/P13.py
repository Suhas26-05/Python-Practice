# Write a program that takes a sentence as input and counts the number of words in it

def count_words(sentence):
    words = sentence.split()
    return len(words)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    word_count = count_words(sentence)
    print(f"Number of words in the sentence: {word_count}")
