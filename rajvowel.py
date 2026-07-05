
def vovel(a):
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        return True
    else:
        return False
    
def main():
    c=input("Enter the character :").lower()
    ret = vovel(c)
    if ret == True :
        print(f"{c} is a vovel")
    else:
        print(f"{c} is a consonent")
if __name__ == "__main__":
    main()
