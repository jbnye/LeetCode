class Solution(object):
    def lengthOfLastWord(self, s):
        ans = 0
        for i in range(len(s) - 1,-1, -1):
            if(s[i] != ' '):
                ans += 1
            else:
                if(ans > 0):
                    return ans
        return ans


# didnt do too well, but I thought mine was simple enough
#can also use split

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.split() seperates all words
#         if len(words) == 0:
#             return 0
#         return len(words[-1])
