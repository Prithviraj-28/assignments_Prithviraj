max_number = lambda a, b , c  : a if a > b and  a > c   else (b if b >c else c)
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    result = max_number(num1, num2,num3)
    print(f"The maximum of {num1} , {num2} and {num3} is {result}")
if __name__ == "__main__":
    main()