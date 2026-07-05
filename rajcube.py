def cube(no):
    return no * no  * no
def main():
    num = int(input("Enter a number: "))
    result = cube(num)
    print(f"The cube of {num} is {result}")   
if __name__ == "__main__":
    main()