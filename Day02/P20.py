 # Implement a program that takes a sentence and a word as input and checks if the word is present in the sentence.

def word_in_Sent(sent, word):
    words = sent.lower().split()
    return word.lower() in words

if __name__ == "__main__":
    sent = input("Enter a sentence: ")
    word = input("Enter the word to search for: ")
    if word_in_Sent(sent, word):
        print(f"The word '{word}' is present in the sentence.")
    else:
        print(f"The word '{word}' is NOT present in the sentence.")
