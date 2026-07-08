multiplication = lambda no1,no2 : no1  *no2
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = multiplication(num1, num2)
    print(f"The multiplication of {num1} and {num2} is {result}")
if __name__ == "__main__":
    main()