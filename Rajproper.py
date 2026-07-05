def proper(no):
    is_divisors= []
    sum = 0
    for i in range(1,no):
        if no % i == 0 :
            is_divisors.append(i)
    
    if no>0 :
        for i in is_divisors:
            sum = sum + i
        
        if sum == no:
            return True

def main():
    a=int(input("Enter the number "))
    ret = proper(a)
    if ret == True:
        print(f"{a} is a proper number ")
    else:
        print(f"{a} is not a proper number ")


if __name__=="__main__":
    main()
