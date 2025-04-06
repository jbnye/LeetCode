class Solution(object):
    def addStrings(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]
        x = 0
        y = 0
        dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,}
        for i in range(max(len(num1),len(num2))):
            if(i < len(num1)):
                x = x + (dic[num1[i]] * pow(10,i))
            if(i < len(num2)):
                y = y + (dic[num2[i]] * pow(10,i))
        
        return str(x + y)