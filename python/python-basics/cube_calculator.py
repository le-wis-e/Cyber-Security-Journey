def main():
    y = int(input("Enter y: "))
    print(f"The cube of {y} is {cube(y)}")

def cube(n):
    return pow(n, 3)

main()    