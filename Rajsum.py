def sum(n):
    sum = 0 
    for i in n:
        sum = sum + int(i)
    return sum

def main():
    a = str(input("Enter the number : "))
    ret = sum(a)
    print("The sum of digits in the number is : ", ret)

if __name__ == "__main__":
    main()