min_number = lambda a, b : a if a < b else b
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = min_number(num1, num2)
    print(f"The minimum of {num1} and {num2} is {result}")
if __name__ == "__main__":
    main()