from functools import reduce
def kami (no):
    result = []
    if no>= 70 and no<=90:
        return no 

def saglya (no):
    add= no+10 
    return add 

def eak(no1,no2): 
    return no1 + no2 

def main():
    p=int(input("Enter the length of the list : "))
    input_list = []
    for i in range(p):
        a=int(input("Enter the number : "))
        input_list.append(a)

    filtered_list = list(filter(kami,input_list))
    mapped_list = list(map(saglya,filtered_list))
    reduced_list = reduce(eak,mapped_list)
    print(f"Filtered list is : {filtered_list}")
    print(f"Mapped list is : {mapped_list}")
    print(f"Reduced  list is : {reduced_list}")

if __name__ == "__main__":
    main()


