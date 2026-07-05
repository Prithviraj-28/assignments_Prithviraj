def area(radius):
    pi = 3.14
    a= pi * radius * radius
    return a 

def main():
    l=int(input("Enter the radius :  "))
    ret = area(l)
    print("The area of circle is ",ret)

if __name__== "__main__":
    main()