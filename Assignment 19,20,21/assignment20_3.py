import time
import threading

def even(no):
    print(f"Tid of even is : {threading.get_ident()}")
    print("Even numbers are : ",end=" ")
    for i in range(1,no+1):
        if i % 2 == 0 :
            print(i, end=",")
    print()
    
def odd(no):
    print(f"Tid of odd is : {threading.get_ident()}")
    print("Odd numbers are : ",end=" ")
    for i in range(1,no+1):
        if i % 2 != 0 :
            print(i,end=",")
    print()

def main():
    print(f"Tid of main is : {threading.get_ident()}")
    number = int(input("Enter the number till which you wanna print even and odd :  "))

    start_time= time.perf_counter() 

    t1obj = threading.Thread(target=even,args=(number,))      #t1 gets created
    t2obj = threading.Thread(target=odd,args=(number,))       #t2 gets created
    t1obj.start()      # t1 started
    t2obj.start()      #t2 started
    t1obj.join()       #t1 joined to main thread so main thread will wait for t1
    t2obj.join()       #t2 joined to main thread so main thread will wait for t2

    end_time = time.perf_counter()

    print(f"Total time required is {end_time-start_time:5f}")   # the :5f will give 5 values after floating point

if __name__ == "__main__":
    main()
