
from functools import reduce 
def is_prime(a):
    if a<=1 :
        return False
    
    for i in range(2,a):
        if a % i == 0:
            return False

    return True
    
square = lambda no : no*2
eak = lambda no1,no2 : no1 if  no1 > no2 else no2
def main():
    p=int(input("Enter the length of the list : "))
    input_list = []
    for i in range(p):
        a=int(input("Enter the number : "))
        input_list.append(a)

    filtered_list = list(filter(is_prime,input_list))
    mapped_list = list(map(square,filtered_list))
    reduced_list = reduce(eak,mapped_list)
    print(f"Filtered list is : {filtered_list}")
    print(f"Mapped list is : {mapped_list}")
    print(f"Reduced  list is : {reduced_list}")

if __name__ == "__main__":
    main()
