check_odd = lambda no : True if no % 2 != 0 else False
def main():
    numbers_list = []
    a=int(input("Enter the number of elements you wanna store in the list : "))

    for i in range(a):
        no1 = int(input("Enter a numbers: "))
        numbers_list.append(no1)
    ret = filter(check_odd,numbers_list)
    print(f"The filter da is {list(ret)}")
    
if __name__ == "__main__":
    main()