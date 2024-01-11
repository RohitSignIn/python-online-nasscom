# Prime Number


def checkPrime(no):
    for i in range(no-1, 1, -1):
        if(no % i == 0):
            return False
        
    return True

print(checkPrime(7))
print(checkPrime(4))
print(checkPrime(5))
print(checkPrime(8))
    