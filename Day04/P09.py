# Write a program that finds the average value of all the elements in a list of dictionaries

def average_value(dicts, key):
    values = [d[key] for d in dicts if key in d]
    return sum(values) / len(values) if values else 0

if __name__ == "__main__":
    dicts = eval(input("Enter list of dictionaries: "))
    key = input("Enter key to average: ")
    print(f"Average value for '{key}': {average_value(dicts, key)}")
