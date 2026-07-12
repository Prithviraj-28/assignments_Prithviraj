def minimum(input_listX):
    min_num = input_listX[0]

    for i in input_listX:
        if i < min_num:
            min_num = i
    
    return min_num
    
def main():
    input_list = list()
    a = int(input("Enter length of list: "))
    for i in range(a):
        num = int(input("Enter number: "))
        input_list.append(num)  
    ret = minimum(input_list)
    print(f"the minimum number in list {input_list} is {ret}")


if __name__ == "__main__":
    main()