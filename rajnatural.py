def natural(no):
    sum = 0
    for i in range(no + 1):
        sum =sum + i
    return sum
def main ():
    no = int(input("Enter a number: "))
    result = natural(no)
    print("The sum of first", no, "natural numbers is:", result)

if __name__ == "__main__":
    main()