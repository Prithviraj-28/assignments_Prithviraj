import threading
def sum(numbers ):
    sumx = 0 
    for i in numbers:
        sumx = sumx + i 
    print(f"Sum of all elements are : {sumx}")

def product(numbers ):
    sumXX = 1 
    for i in numbers:
        sumXX = sumXX * i 
    print(f"Sum of all elements are : {sumXX}") 

def main():
    numbers=[]
    p = int(input("Enter the nummbers you want to add to the list : "))
    for i in range(p):
        A = int(input("Enter the number : "))
        numbers.append(A)

    # Creating the two threads
    t1 = threading.Thread(target=sum, args=(numbers,), name="sum")  #name="Prime" assigns Prime name to thread t1
    t2 = threading.Thread(target=product, args=(numbers,), name="product")  #name="Nonprime" assigns Prime name to thread t2

    # Starting both threads
    t1.start()
    t2.start()

    # Waiting for threads to finish
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()