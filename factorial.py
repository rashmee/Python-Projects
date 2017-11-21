# coding=utf-8
# Factorial of a number

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        return res

n = input("Enter number? ")
print(factorial(n))