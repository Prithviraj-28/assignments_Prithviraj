def area(len,wid):
    a= len * wid
    return a 

def main():
    l=int(input("Enter the Length :  "))
    w= int(input("Enter the width : "))
    ret = area(l,w)
    print("The area of rectangle is ",ret)

if __name__== "__main__":
    main()
