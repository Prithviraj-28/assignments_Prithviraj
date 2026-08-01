mult = lambda no1,no2 : no1 * no2

def main():
    number1= int(input("Enter  first number : "))
    number2= int(input("Enter second number : "))
    ret = mult(number1,number2)
    print(f"The Multiplication  of {number1} and {number2} is {ret}")

if __name__ == "__main__":
    main()