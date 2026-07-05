def multtable(n):
    for i in range (1,11):
        multiplication = n * i
        print(n, "x", i, "=", multiplication)

def main():
    num = int(input("Enter a number to print its multiplication table: "))
    multtable(num)

if __name__ == "__main__":
    main()