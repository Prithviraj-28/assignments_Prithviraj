square = lambda no : no ** 2 
def main():
    num = int(input("Enter a number: "))
    result = square(num)
    print(f"The square of {num} is {result}")
if __name__ == "__main__":
    main()