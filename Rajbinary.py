def binary_convert(n):
    number=[]
    reversenumber=[]

    while n > 0:
        remainder = n % 2
        number.append(remainder)
        n = n//2

    for i in range(len(number)-1,-1,-1):
        reversenumber.append(number[i])

    return reversenumber

def main():
    a= int (input("Enter the number: "))
    ret = binary_convert(a)
    print(f"{a} binary equivalent is ", ret)

if __name__ == "__main__":
    main()

