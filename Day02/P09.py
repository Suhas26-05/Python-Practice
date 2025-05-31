# Implement a function to check if a given year is a leap year or not

def Leap_or_not(num):
    if ( num % 4 == 0 and num % 100 != 0 ) or (num % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Enter the Year: "))
    val = Leap_or_not(num)

    if val == True:
        print(f"Given year {num} is Leap Year")
    else:
        print(f"Given year {num} is not Leap Year")