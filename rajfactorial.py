def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    return fact

def main():

    n=int(input("Enter a number: "))
    result=factorial(n)
    print("The factorial of",n,"is:",result)

if __name__ == "__main__":
    main()