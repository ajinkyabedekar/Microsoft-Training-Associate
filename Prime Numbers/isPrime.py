from math import sqrt
import os


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def num_input():
    while True:
        try:
            num = -1
            count2 = 0
            while num < 0:
                if count2 > 0:
                    print("Enter a positive number please!!!!!!")
                num = int(input("Enter a positive number to find out whether the number is a prime or non-prime : "))
                count2 = count2 + 1
        except ValueError:
            print("You must enter an integer.")
        else:
            return num


while True:
    print("\t\t isPrime.exe \n")
    number = num_input()
    check = is_prime(number)
    if check:
        print(str(number) + " is a prime number")
    else:
        print(str(number) + " is not a prime number")

    yon = 'a'
    count = 0
    while yon != ['Y', 'N']:

        if count > 0:
            print("Enter a valid option please!!!")
        yon = input("Do you want to continue using isPrime.exe (Y/N) : ").upper()
        count = count + 1
        if yon == 'N':
            exit(0)
        elif yon == 'Y':
            os.system('cls')
            break
        else:
            continue