def count(name):
    sum = 0 
    for i in range(len(name)):
        sum = sum + 1
    return sum
def main():
    a=str(input("Enter the name : "))
    ret = count(a)
    print(f"{a} has {ret} characters")
if __name__ == "__main__":
    main()
