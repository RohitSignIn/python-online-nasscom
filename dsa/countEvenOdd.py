a = [1,7,3,4,5,6,7,8,9,10]

countEven = 0
countOdd = 0

for i in a:
    if(i % 2 == 0):
        countEven += 1
    else:
        countOdd += 1

print("Count of Even Nums:", countEven)
print("Count of Odd Nums:", countOdd)
