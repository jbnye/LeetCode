class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        ans = 0
        dic = {}
        for dom in dominoes:
            key = tuple(sorted(dom))
            if(key in dic):
                ans += dic[key]
                dic[key] += 1
            else:
                dic[key] = 1
        
        return ans