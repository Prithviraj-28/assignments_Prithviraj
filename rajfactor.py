#write a programm which accepts a number and prints its factors 
# input = 12
# output = 1,2,3,4,6,12

def factors(a):
    result=[]
    for i in range(1,a+1):
        if a % i == 0 :
            result.append(i)
    return result 

def main ():
    a= int(input("Enter the number : "))
    ret = factors(a)
    print(f"Factors of {a} are : ",ret)

if __name__ == "__main__":
    main()
    