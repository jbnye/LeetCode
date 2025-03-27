class Solution(object):
    def sumOfSquares(self, nums):
        ans = 0
        i = 1
        for n in nums:
            if len(nums) % i == 0:
                ans = ans + (nums[i - 1] * nums[i - 1])
            i += 1
        return ans

        