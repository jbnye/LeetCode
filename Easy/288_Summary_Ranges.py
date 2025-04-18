class Solution(object):
    def summaryRanges(self, nums):
        ans = []
        if not nums:
            return []
        left, right = nums[0], nums[0]

        for i in range(1, len(nums)):
            if(nums[i] > right + 1):
                if(left != right):
                    ans.append(str(left) + "->" + str(right))
                else:
                    ans.append(str(left))
                left, right = nums[i], nums[i]
            else:
                right = nums[i]

        if(left != right):
            ans.append(str(left) + "->" + str(right))
        else:
            ans.append(str(left))
        return ans
