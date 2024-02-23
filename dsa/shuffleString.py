def shuffleStr(s, indices):
    dummyList = [None] * len(s)
    i = 0
    while(i < len(s)):
        char = s[i]
        belongsTo = indices[i]

        dummyList[belongsTo] = char

        i+=1

    res = ""
    for i in dummyList:
        res = res + i

    return res

print(shuffleStr("codeleet", [4,5,6,7,0,2,1,3]))