def checkevenodd(no):
    if no % 2 == 0 :
        return True
    else:
        return False

def main():
    a=int(input("Enter the number: "))
    ret=checkevenodd(a)
    if ret==True:
        print(f"{a} is an even number")
    else:
        print(f"{a} is an odd number")

if __name__ == "__main__":
    main()