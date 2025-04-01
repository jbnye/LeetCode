class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        dic = {}
        for index, num in enumerate(nums):
            if((target - num) in dic):
                ans.append(index)
                ans.append(dic[(target - num)])
                return ans
            dic[num] = index
            
        return ans

array = [2,11,7,15]
sol = Solution()
print(sol.twoSum(array, 9))