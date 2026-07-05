def grade(name, a, b, c, d, e):
    x=(a+b+c+d+e)/500 * 100
    if x>= 95:
        print(f'Congratulations {name} your grade is A+')
    elif x>= 90:
        print(f'Congratulations {name} your grade is A')
    elif x>= 85:
        print(f'Congratulations {name} your grade is B+')
    elif x>= 80:
        print(f'Congratulations {name} your grade is B')
    elif x>= 75:
        print(f'Congratulations {name} your grade is C+')
    elif x>= 70:
        print(f'{name} your grade is C+')
    elif x>= 65:
        print(f' {name} your grade is C')
    elif x>= 60:
        print(f'{name} your grade is D+')
    elif x>= 55:
        print(f'{name} your grade is D')
    elif x>= 50:
        print(f'{name} your grade is D')

    else:
        print(f'Sorry {name} your grade is F better luck next time')

def main():
    print('                                     Welcome to Bhegade Internationa School ')   
    name=input('Enter Your Name :').strip().title()
    print('Enter marks in all subjects out of 100')
    a=float(input('Enter Your marks in Maths :'))
    b=float(input('Enter Your marks in English :'))
    c=float(input('Enter Your marks in Hindi :'))
    d=float(input('Enter Your marks in Science :'))
    e=float(input('Enter Your marks in Social Science :'))
    grade(name, a, b, c, d, e)

if __name__ == "__main__":
    main()