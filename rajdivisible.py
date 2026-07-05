def divisible(no):
    if no%3 == 0 and no%5==0:
        print(f"{no} is divisible by 3 and 5")
    else:
        print(f"{no} is not divisible by 3 and 5")

def main():
    a = int(input("Enter  number : "))
    divisible(a)

if __name__== "__main__":
    main()
