def print_star(no):
    for i in range(no):
        print("*",end = "   ")

def main():
    a=int(input("Enter the number of times to display: "))
    print_star(a)
if __name__ == "__main__":
    main()