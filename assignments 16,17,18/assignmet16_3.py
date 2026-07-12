def addition(no1, no2):
    return no1 + no2
def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    ret=addition(a,b)
    print(f"Addition of {a} and {b} is: {ret}")
if __name__ == "__main__":
    main()