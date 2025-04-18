def convertToTitle( columnNumber):
    x = columnNumber
    ans = ""
    while (x != 0):
        num = x % 26
        if(num!=0):
            ans = chr(num+ 64) + ans
            x = x // 26
        else:
            ans = "Z" + ans
            x = (x // 26) - 1

    
    return ans


print(convertToTitle(701))