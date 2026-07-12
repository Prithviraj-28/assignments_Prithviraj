def display(no):
    for i in range(no,0,-1):
        print(i,end = " ")

def main():
    a=int(input("Enter the number of times to display: "))
    display(a)
    
if __name__ == "__main__":
    main()