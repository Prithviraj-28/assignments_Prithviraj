check_even = lambda no : True if no % 2 == 0 else False
def main():
    num = int(input("Enter a number: "))
    result = check_even(num)
    if result == True :
        print(f"{num} is even")
    else :
        print(f"{num}is odd")
if __name__ == "__main__":
    main()