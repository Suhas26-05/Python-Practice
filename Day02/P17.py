# Create a function that takes a sentence as input and returns the sentence in reverse order.

def reverse(sente):
    words = sente.split()      
    reversed_words = words[::-1]  
    return ' '.join(reversed_words)

if __name__ == "__main__":
    sent = input("Enter a sentence: ")

    print(f"Reverse of String is {reverse(sent)}")