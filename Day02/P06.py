# Calculate the area of a triangle given its base and height using a function

def AOT(Hei, Bas):
    return Hei * Bas * 0.5

if __name__ == "__main__":
    Hei = float(input("Enter the Height of Triangle: "))
    Bas = float(input("Enter the Base of Triangle: "))

    c = AOT(Hei, Bas)

    print(f"Area of Triangle is {c}")