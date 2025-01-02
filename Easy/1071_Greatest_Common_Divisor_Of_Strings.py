class Solution(object):
    def gcdOfStrings(self, str1, str2):
        ans =  ""
        if(str1 + str2) != (str2 + str1):
            return ""
        if (len(str1) < len(str2)):
            str1, str2 = str2, str1
        for x in range(len(str2), 0, -1):
            if((len(str1) % x) == 0) and ((len(str2) % x) == 0):
               return str2[:x] 