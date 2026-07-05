def print_number(no):
    result = []
    for i in range(no,0,-1):
        result.append(i)
    return result
def main():
    a= int(input("Enter the NUmber : "))
    ret = print_number(a)
    print(f"All numbers starting from 1 to {a} are : ",ret)

if __name__ == "__main__":
    main()