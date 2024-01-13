def reverseString(str):
    revStr = ""
    for i in str:
        revStr = i + revStr

    return revStr

def checkPalindrome(str):
    if(str == reverseString(str)):
        return True
    else:
        return False
    
print(checkPalindrome("racecar"))
    