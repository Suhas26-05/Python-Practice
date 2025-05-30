# Calculate the compound interest for a given principal, rate, and time

def Cal_compound_interest(principal, rate, time):
    amo = principal * (1 + 1/rate) ** time
    compound_interest = amo - principal
    print(f"Compound Interest of given principal, rate, and time is {compound_interest}")

if __name__ == "__main__":
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Rate of Interest: "))
    time = float(input("Enter Time in Years: "))

    Cal_compound_interest(principal, rate, time)