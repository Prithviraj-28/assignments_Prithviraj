def display(rows):
    for i in range(rows):
        for j in range(i+1,rows+1):
            print(j, end=" ")
        print()
def main():
    rows = int(input("Enter number of rows: "))

    display(rows)
if __name__ == "__main__":
    main()