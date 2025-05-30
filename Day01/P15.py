# Given a list of names, print all names starting with the letter 'A'.

def List_names(names):
    A_names = []

    for i in names:
        if i.startswith("A"):
            A_names.append(i)

    return A_names

if __name__ == "__main__":
    names = input("Enter names separated by spaces: ").split()
    A = List_names(names)
    print("Names starting with 'A':", A)