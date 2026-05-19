# def meaning define is used to create functions e.g hello
def main():
    name = input("Enter name: ").capitalize()
    x = int(input("Enter x: "))
    hello(name)
    print("The square of x is,", square(x))


def hello(to):
    print("Hello,", to)

def square(n):
    return (n * n)    


main()
