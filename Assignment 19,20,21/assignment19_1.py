square = lambda no1 : no1 ** 2

def main():
    number= int(input("Enter the number : "))
    ret = square(number)
    print(f"The square of {number} is {ret}")

if __name__ == "__main__":
    main()