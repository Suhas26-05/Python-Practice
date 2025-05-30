# Convert a given number of days into years, weeks, and days.

def Convert(TDays):
    year = TDays//365
    remaining_day = TDays % 365
    weeks = remaining_day // 7
    days = remaining_day % 7

    print(f"{TDays} days into years, weeks, and days is {year}, {weeks}, {days}")


if __name__ == "__main__":
    TDays = int(input("Enter a Number: "))
    Convert(TDays)