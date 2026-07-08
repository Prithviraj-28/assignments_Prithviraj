square = lambda no1 : no1 ** 2
def main():
    numbers_list = []
    a=int(input("Enter the number of elements you wanna store in the list : "))

    for i in range(a):
        no1 = int(input("Enter a numbers: "))
        numbers_list.append(no1)

    ret = map(square, numbers_list)
    print("The square of the numbers is: ", list(ret))

if __name__ == "__main__":
    main()
