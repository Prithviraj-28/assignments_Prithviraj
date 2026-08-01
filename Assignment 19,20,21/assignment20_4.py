import threading
def small(text):
    lowercase_count = 0
    for char in text:
        if char.islower():
            lowercase_count = lowercase_count + 1
    print(f"Lowercase characters: {lowercase_count}")

def capital(text):
    uppercase_count = 0
    for char in text:
        if char.isupper():
            uppercase_count=uppercase_count + 1
    print(f"Uppercase characters: {uppercase_count}")

def digits(text):
    digit_count = 0
    for char in text:
        if char.isdigit():
            digit_count = digit_count + 1 
    print(f"Digits: {digit_count}")

def main():
    user_input = input("Enter a string: ")

    t1obj = threading.Thread(target=small,args=(user_input,))

    t2obj = threading.Thread(target=capital,args=(user_input,))

    t3obj = threading.Thread(target=digits,args=(user_input,))

    t1obj.start()
    t2obj.start()
    t3obj.start()
    t1obj.join()
    t2obj.join()
    t3obj.join()

if __name__ == "__main__":
    main()


    


