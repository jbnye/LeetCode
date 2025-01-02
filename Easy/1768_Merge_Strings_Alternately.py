class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        i = len(word1)
        j = len(word2)
        x = 0
        while (x < i) or (x < j):
            if(x < i):
                ans = ans + word1[x]
            if(x < j):
                ans = ans + word2[x]
            x += 1
        return ans