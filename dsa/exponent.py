# 11. Display Power (Exponent)
def getPower(no, power):
    powerGot = 1
    for i in range(power):
        powerGot = powerGot*no

    return powerGot

print(getPower(2, 3))