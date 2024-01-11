# Factorial

def factorial(no):
    fact = 1

    while(no>1):
        fact = fact * no
        no -= 1

    return fact


print(factorial(5))