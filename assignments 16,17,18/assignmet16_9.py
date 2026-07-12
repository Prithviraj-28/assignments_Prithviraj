def print_even(no):
    for i in range(1,no+1):
        if i % 2 == 0:
            print(i,end = " ")
def main():
    a=int(input("Enter the number of times to display: "))
    print_even(a)
if __name__ == "__main__":
    main()