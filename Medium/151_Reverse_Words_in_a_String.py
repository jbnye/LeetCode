# my solution
class Solution(object):
    def reverseWords(self, s):
        arr = []
        ans = ""
        builder = ""
        for x in range(len(s)):
            if(s[x] != ' '):
                builder += s[x]
            if((s[x] == ' ') and (builder != "")):
                arr.append(builder)
                builder = "" 
        if(builder):
            arr.append(builder)
        arr.reverse()
        for x in range(len(arr)):
            ans += arr[x]
            if(x != (len(arr) -1)):
                ans += " "
        return ans