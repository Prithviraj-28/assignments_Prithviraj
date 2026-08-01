import threading
def maximum(numbers):
    max_num = numbers[0] 
    for i in numbers:
        if i > max_num:
            max_num = i 
    print(f"Maximum number in the list is :  {max_num}")

def mminimum(numbers):
    min_num = numbers[0] 
    for i in numbers:
        if i < min_num :
            min_num = i 

    print(f"Minimum number in the list is :  {min_num}")

def main():
    numbers=[]
    p = int(input("Enter the nummbers you want to add to the list : "))
    for i in range(p):
        A = int(input("Enter the number : "))
        numbers.append(A)

    t1 = threading.Thread(target= maximum , args=(numbers,), name= "MAX_NUM")
    t2 = threading.Thread(target= mminimum , args=(numbers,), name= "MIN_NUM")

    # Starting both threads
    t1.start()
    t2.start()
    
    # Waiting for threads to finish
    t1.join()
    t2.join()
    
if __name__ == "__main__":
        main()
