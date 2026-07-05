def checkodd(no):
    for i in range(1,no+1):
        if i % 2 != 0 :
            print(i)

def main():
    a = int(input("Enter the number :"))
    checkodd(a)

if __name__ == "__main__":
    main()