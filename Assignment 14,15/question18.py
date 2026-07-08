check_list = lambda no : True if no % 3 == 0 and no%5 == 0 else False
def main():
    numbers_list = []
    a=int(input("Enter the number of elements you wanna store in the list : "))

    for i in range(a):
        no1 = int(input("Enter a numbers: "))
        numbers_list.append(no1)
    ret = filter(check_list,numbers_list)
    print(f"The filter daata is {list(ret)}")
    
if __name__ == "__main__":
    main()