def count_numbers(n):
    sum = 0
    for i in range (len(n)):
        sum = sum + 1
    return sum

def main():
    a = str(input("Enter a number: "))
    result = count_numbers(a)
    print("The count of numbers is:", result)

if __name__ == "__main__":
    main()