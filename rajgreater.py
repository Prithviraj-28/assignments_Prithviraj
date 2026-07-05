def greater(no1,no2):
    if no1>no2:
        print(f"{no1} is greater")
    elif no1<no2:
        print(f"{no2} is greater")
    else:
        print("Both numbers are equal")
def main():
    a = int(input("Enter  first number : "))
    b = int(input("Enter  second number : "))
    greater(a, b)

if __name__== "__main__":
    main()