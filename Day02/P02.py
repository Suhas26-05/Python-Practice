# Write a Python function to check if a given string is a palindrome

def Palindrome(string):
    if string[0::] == string[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    string = input("Enter a String: ")
    x = Palindrome(string)
    print(x)
    if x == True:
        print(f"Given String {string} is a Palindrome")
    else:
        print(f"Given String {string} is not a Palindrome") 