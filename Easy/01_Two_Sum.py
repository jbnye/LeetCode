class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = []
        m = {}
        for i in range(len(nums)):
            if target - nums[i] in m:
                ans.append(m[target - nums[i]])
                ans.append(i)
            else:
                m[nums[i]] = i
        return ans