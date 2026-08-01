import time
import threading

def Evenfactor (no):
    print(f"Tid of even is : {threading.get_ident()}")
    factors = []
    for i in range(1,no+1):
        if no%i == 0:
            factors.append(i)

    evenfact = []
    for i in factors:
        if i%2 == 0:
            evenfact.append(i)

    total = 0 
    for i in evenfact:
        total = total+i

    print(f"The addition of even factors is {total}")

def oddfactor (no):
    print(f"Tid of odd is : {threading.get_ident()}")
    factors = []
    for i in range(1,no+1):
        if no%i == 0:
            factors.append(i)

    oddfact = []
    for i in factors:
        if i%2 != 0:
            oddfact.append(i)

    total = 0 
    for i in oddfact:
        total = total+i

    print(f"The addition of odd factors is {total}")

def main():
    print(f"Tid of main is : {threading.get_ident()}")
    number = int(input("Enter the number for the even and odd factors :  "))

    start_time= time.perf_counter() 

    t1obj = threading.Thread(target=Evenfactor,args=(number,))      #t1 gets created
    t2obj = threading.Thread(target=oddfactor,args=(number,))       #t2 gets created
    t1obj.start()      # t1 started
    t2obj.start()      #t2 started
    t1obj.join()       #t1 joined to main thread so main thread will wait for t1
    t2obj.join()       #t2 joined to main thread so main thread will wait for t2

    end_time = time.perf_counter()

    print(f"Total time required is {end_time-start_time:5f}")
if __name__ == "__main__":
    main()
