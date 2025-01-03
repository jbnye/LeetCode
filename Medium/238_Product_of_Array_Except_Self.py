# my solution
class Solution(object):
    def productExceptSelf(self, nums):
        arr = []
        for x in range(len(nums)):
            ans = 1
            for y in range(len(nums)):
                if(y != x):
                    ans = ans * nums[y]
            arr.append(ans)
        return arr
    

# the cringe solution
class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in xrange(1, len(nums)): # from left to right 
            res[i] = res[i-1] * nums[i-1]
        tmp = 1
        for i in xrange(len(nums)-2, -1, -1): # from right to left
            tmp *= nums[i+1]
            res[i] *= tmp
        return res