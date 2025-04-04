
def addBinary(a, b):

    result = ""
    a = a[::-1]
    b = b[::-1]
    carry = 0
    for i in range(max(len(a),len(b))):
        digitA = int(a[i]) if i < len(a) else 0
        digitB = int(b[i]) if i < len(b) else 0
        total = digitA + digitB + carry
        char = str(total % 2)
        result = char + result
        carry = total // 2
            
    if(carry != 0):
        result =  "1" + result
    return result

a = "11"
b = "1"
print(addBinary(a, b))

# 0ms solution using BIN
# class Solution(object):
#     def addBinary(self, a, b):
#         return bin(int(a, 2) + int(b, 2))[2:]



    # Intial try 6% Time 85% space
    # sum1 = 0
    # sum2 = 0
    # if(len(a) >= len(b)):
    #     max = len(a) +1
    # else:
    #     max = len(b)+ 1
    # ans = ""
    # for x in range(len(a)):
    #     if(a[x] == "1"):
    #         sum1 = sum1 + pow(2, (len(a)-x)- 1)
    # for x in range(len(b)):
    #     if(b[x] == "1"):
    #         sum2 = sum2 + pow(2, (len(b)-x)- 1)

    # total = sum1 + sum2
    # if(total == 0):
    #     return "0"
    # while(total != 0):
    #     if(total - (pow(2, max)) == 0):
    #         ans = ans + "1" + "0" * max
    #         return ans
    #     if(total - (pow(2,max)) < 0):
    #         max = max - 1
    #         if(len(ans) > 0):
    #             ans += "0"
    #     else:
    #         total = total  - pow(2,max)
    #         max -= 1
    #         ans += "1"


    # return ans