def frequency(input_listX,a):
    number_freq = 0

    for i in input_listX:
        if i == a :
            number_freq = number_freq + 1
    return number_freq
    
def main():
    input_list = list()
    a = int(input("Enter length of list: "))
    for i in range(a):
        num = int(input("Enter number: "))
        input_list.append(num)  
    search= int(input("enter the element to search : "))
    ret= frequency(input_list,search)
    print(f"The frequency of {search} in {input_list} is {ret}")


if __name__ == "__main__":
    main()