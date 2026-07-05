def print_number(no):
    result = []
    for i in range(1,no+1):
        result.append(i)
    return result
def main():
    a= int(input("Enter the NUmber : "))
    ret = print_number(a)
    print(f"All numbers starting from 1 to {a} are : ",ret)

if __name__ == "__main__":
    main()

