# Create a program that generates the Fibonacci sequence up to a given number of terms.

def Fibo(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

if __name__ == "__main__":

    n = int(input("Enter a Number:")) 
    f = Fibo(n)

    print("Fibonacci sequence", f)

