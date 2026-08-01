import threading

def display_prime(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                primes.append(num)
    print("Prime numbers:", *primes,sep=",")  # the *before list name returns list without bracket and sep="," seperateds the list by ,

def display_non_prime(numbers):
    non_primes = []
    for num in numbers:
        if num <= 1:
            non_primes.append(num)
        else:
            for i in range(2, num):
                if num % i == 0:
                    non_primes.append(num)
                    break
    print("Non-Prime numbers:", *non_primes,sep=",")  # the *before list name returns list without bracket and sep="," seperateds the list by ,

def main():
    numbers=[]
    p = int(input("Enter the nummbers you want to add to the list : "))
    for i in range(p):
        A = int(input("Enter the number"))
        numbers.append(A)

    # Creating the two threads
    t1 = threading.Thread(target=display_prime, args=(numbers,), name="Prime")  #name="Prime" assigns Prime name to thread t1
    t2 = threading.Thread(target=display_non_prime, args=(numbers,), name="NonPrime")  #name="Nonprime" assigns Prime name to thread t2

    # Starting both threads
    t1.start()
    t2.start()

    # Waiting for threads to finish
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

        