from functools import reduce
sum = lambda x, y: x + y

def main():
    input_list = list()
    a = int(input("Enter length of list: "))
    for i in range(a):
        num = int(input("Enter number: "))
        input_list.append(num)  
    ret = reduce(sum, input_list)
    print(f"The sum of the numbers in the list is: {ret}")

if __name__ == "__main__":
    main()
