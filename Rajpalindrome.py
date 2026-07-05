def is_palindrome(s):
    a = len(s)
    result = []
    for i in range(a,0,-1):
        result.append(s[i-1])   #reverse number logic 
    if result == list(s):
        return True

def main():
    input_str = str(input("Enter the number: ") )
    p= is_palindrome(input_str)
    if p==True:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")    


if __name__ == "__main__":
    main()