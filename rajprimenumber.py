#programm to find prime number ; a number which is divisible by itself only no other divisors
#input = 11
#output = prime number 
def is_prime(a):
    if a<=1 :
        return False
    
    for i in range(2,a):
        if a % i == 0:
            return False
    
def main():
    a=int(input("Enter the number : "))
    ret=is_prime(a)
    if ret==False:
        print("It is not a prime number")
    else:
        print("It is a prime number")

if __name__ == "__main__":
    main()


