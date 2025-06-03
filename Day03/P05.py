# Given a list of words, find the word with the maximum length and its length

def Max_leng(lis):
    if not lis:
        return None, 0  # Handle empty list
    max_word = max(lis, key=len)
    return max_word, len(max_word)

if __name__ == "__main__":
    lis = input("Enter names separated by spaces: ").split()
    print(f"maximum length and its length is for Given List is {Max_leng(lis)}")