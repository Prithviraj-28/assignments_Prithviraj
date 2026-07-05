def Addition(No1,No2):
    Ans=No1+No2
    print(f"Addition of {No1} and {No2} is : ",Ans)

def Substraction(No1,No2):
    Ans=No1-No2
    print(f"Substraction of {No1} and {No2} is : ",Ans)

def Multiplication(No1,No2):
    Ans=No1*No2
    print(f"Multiplication of {No1} and {No2} is : ",Ans)

def Divsion(No1,No2):
    Ans=No1// No2  #// gives the output of division as an integer
    print(f"Division of {No1} and {No2} is : ",Ans)

def main():
    number1 = int(input("Enter the  first number :"))
    number2 = int (input("Enter the second number : "))
    Addition(number1,number2)
    Substraction(number1,number2)
    Multiplication(number1,number2)
    Divsion(number1,number2)

if __name__ == "__main__":
    main()
