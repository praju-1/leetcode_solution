"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x
"""
def power_of_three(num):
    try:
        if num < 1:
            print("\nEnter positive number only")
            return False
        
        while num % 3 == 0:
            num //= 3
        
        return num == 1
    except Exception as e:
        print(e)
        return False

try:
    n = int(input("Enter any number to check: "))
    if power_of_three(n):
        print("True")
    else:
        print("False")
except ValueError:
    print("Please enter a valid integer")
except Exception as e:
    print(e)
