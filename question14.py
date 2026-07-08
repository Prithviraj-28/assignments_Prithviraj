from functools import reduce
addition= lambda no1,no2: no1 + no2 
numbers_list = []
def main():
    a=int(input("Enter the number of elements you wanna store in the list : "))

    for i in range(a):
        no1 = int(input("Enter a numbers: "))
        numbers_list.append(no1)
    ret = reduce(addition, numbers_list)
    print(f"The addition of {numbers_list} is {ret}")

if __name__ == "__main__":
    main()