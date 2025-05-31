# Given a list of names, count the number of names that start with a vowel

def Star_Vow(names):
    vowels = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
    Vow_names = []

    for i in names:
        if i.startswith(vowels):
            Vow_names.append(i)

    return len(Vow_names)

if __name__ == "__main__":
    names = input("Enter names separated by spaces: ").split()
    print(f"Names starting with a vowel: {Star_Vow(names)}")