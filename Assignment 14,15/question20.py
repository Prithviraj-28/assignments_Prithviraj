check_even = lambda no : True if no % 2 == 0 else False
def main():
    numbers_list = []
    a=int(input("Enter the number of elements you wanna store in the list : "))

    for i in range(a):
        no1 = int(input("Enter a numbers: "))
        numbers_list.append(no1)
    ret = filter(check_even,numbers_list)
    count= len(list(ret))

    print(f"The count of even numbers in the list is {count}")
    
if __name__ == "__main__":
    main()