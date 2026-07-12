def check(no):
    if no < 0:
        print(f"Input : {no}",end = "            ")
        print(f"Output : Negative number")
    elif no > 0:
        print(f"Input : {no}",end = "            ")
        print(f"Output : Positive number")
    else:
        print(f"Input : {no}",end = "            ")
        print(f"Output : Zero")
def main():
    a=int(input("Enter the number: "))
    check(a)
if __name__ == "__main__":
    main()