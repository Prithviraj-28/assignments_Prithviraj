task= lambda word: len(word) > 5
def main():
    user_input = input("Enter a list of words separated by spaces: ")
    word_list = user_input.split()
    ret = filter(task , word_list)
    print("Words with more than 5 letters:",list(ret))

if __name__ == "__main__":
    main()
