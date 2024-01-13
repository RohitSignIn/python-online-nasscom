def getPower(no, power):
    no = int(no)

    pow = 1
    while(power):
        pow = pow * no
        power-=1

    return pow

def checkArmstrong(no):
    power = len(str(no))
    res = 0
    for i in str(no):
        res += getPower(i, power)

    if(no == res):
        return True
    
    return False



print(checkArmstrong(153))