# Create a program that takes a user's name and age as input and prints a greeting message.

def greetings(name, age):
    print(f"What's up,{name}? {age} years of awesome! Ready for something fun today?")

if __name__ == "__main__":
    name = input("Enter your Name: ")
    age = int(input("Enter your age: "))
    greetings(name,age)