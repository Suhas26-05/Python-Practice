# Implement a function that takes a list of numbers and returns a new list with the squared values

def Squ_Lis(lis):
    for i in range(len(lis)):
        lis[i] = lis[i] ** 2
    return lis

if __name__ == "__main__":
    lis = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(f"Square of Given List is {Squ_Lis(lis)}")

     