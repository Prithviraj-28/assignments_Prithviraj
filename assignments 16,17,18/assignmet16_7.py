def checkdivisible(no):
    if no % 5 == 0 :
        return True
    else:
        return False

def main():
    a=int(input("Enter the number: "))
    ret=checkdivisible(a)
    if ret==True:
        print("Input : ",a,end = "            ")
        print(" output: True")
    else:
        print("Input : ",a,end = "            ")
        print(" Output: False")

if __name__ == "__main__":
    main()