def reverse(n):
    a=len(n)
    result=[]
    for i in range (a,0,-1):
        result.append(n[i-1])
    return result

def main():
    a=str(input("Enter the number: "))
    ret = reverse(a)
    print("The reversed number is: ", str(ret))

if __name__ == "__main__":
    main()