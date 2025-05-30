# Create a program that counts the number of words in a sentence

def count_word(string):
    word = string.split()
    return len(word)

if __name__ == "__main__":
    string = input("Enter a Sentence: \n")
    x = count_word(string)
    print(f"The total count of words in a given sentence is {x}")