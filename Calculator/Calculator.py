def add(a,b):
    return (a+b)
def subtract(a,b):
    return (a-b)
def multiply(a,b):
    return (a*b)
def divide(a,b):
    return (a/b)
while True:
    print("\n-:MENU:-\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
    try:
        ch = int(input("Enter Your Choice: "))
        if ch is 1:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            addition = add(a,b)
            print(addition)
        elif ch is 2:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            subtraction = subtract(a,b)
            print(subtraction)
        elif ch is 3:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            multiplication = multiply(a,b)
            print(multiplication)
        elif ch is 4:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            try:
                division = divide(a,b)
                print(division)
            except ZeroDivisionError:
                print("Division by Zero is not Possible")
        else:
            print("Invalid Choice")
    except ValueError:
        print("Please Provide Integers for Operations")
    while True:
        wtc = input("Want to Continue?(Y/N) ")
        if wtc in ['y','Y']:
            flag = True
            break
        elif wtc in ['n','N']:
            flag = False
            break
        else:
            print("Please Enter Y/N")
            continue
    if flag:
        continue
    else:
        break