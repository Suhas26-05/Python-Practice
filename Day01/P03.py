# Create a function to check if a given string is a palindrome.

def Palindrome(s):
    if s[0::] == s[::-1]:
        print(f"Given String or {s} is a Palindrome")
    else:    
        print(f"Given String or {s} is not a Palindrome")


if __name__ == "__main__":
    s = input("Enter a String: ")
    Palindrome(s)