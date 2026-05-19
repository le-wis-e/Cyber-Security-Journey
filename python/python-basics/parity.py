def main():
    x = int(input("Enter the value is x: "))
    if is_even(x):
        print(f"{x} is an even number ")
    else:
        print(f"{x} is an odd  number")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()