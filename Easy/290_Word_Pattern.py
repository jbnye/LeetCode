class Solution(object):
    def wordPattern(self, pattern, s):
        dic = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for index, word in enumerate(words):
            if(pattern[index] not in dic.keys()):
                if(word in dic.values()):
                    return False
                else:
                    dic[pattern[index]] = word
            else:
                if(dic[pattern[index]] != word):
                    return False

        return True 

sol = Solution()
pattern = "abba"
s = "dog dog dog dog"
print(sol.wordPattern(pattern, s))