# Given two lists of numbers, concatenate them into a single list.

def Comb_List(lis1, lis2):
    return lis1 + lis2

if __name__ == "__main__":
    lis1 = list(map(int, input("Enter numbers separated by spaces: ").split()))
    lis2 = list(map(int, input("Enter numbers separated by spaces: ").split()))
    x = Comb_List(lis1, lis2)
    print(f"concatenate of two Give list is {x}")