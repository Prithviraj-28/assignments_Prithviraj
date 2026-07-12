def factors(a):
    sum= 0 
    for i in range(1,a):
        if a % i == 0 :
            sum = sum + i
    return sum
 
def main ():
    a= int(input("Enter the number : "))
    ret = factors(a)
    print(f"Factors of {a} are : ",ret)

if __name__ == "__main__":
    main()