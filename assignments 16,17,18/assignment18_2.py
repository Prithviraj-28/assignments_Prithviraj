def maximum(input_listX):
    max_num = input_listX[0]

    for i in input_listX:
        if i > max_num:
            max_num = i
    
    return max_num
    
def main():
    input_list = list()
    a = int(input("Enter length of list: "))
    for i in range(a):
        num = int(input("Enter number: "))
        input_list.append(num)  
    ret = maximum(input_list)
    print(f"the maximum number in list {input_list} is {ret}")


if __name__ == "__main__":
    main()