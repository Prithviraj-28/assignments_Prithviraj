check_odd = lambda no : no % 2 != 0 
def main():
    num = int(input("Enter a number: "))
    result = check_odd(num)
    print(result)
   
if __name__ == "__main__":
    main()