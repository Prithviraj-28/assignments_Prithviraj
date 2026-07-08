check_divisible = lambda no : no % 5 == 0 
def main():
    num = int(input("Enter a number: "))
    result = check_divisible(num)
    print(result)
   
if __name__ == "__main__":
    main()