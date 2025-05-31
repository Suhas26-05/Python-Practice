# Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly

def Even_or_Odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":

    num = int(input("Enter the a Number: "))
    if Even_or_Odd(num) == True:
        print(f"Given {num} Number is Even")
    else:
        print(f"Given {num} Number is Odd")