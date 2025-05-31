# Create a function to reverse a given string

def reverse(string):
    return string[::-1]

if __name__ == "__main__":
    string = input("Enter words separated by spaces: ")
    print(f"Reverse of Given String is {reverse(string)}")
