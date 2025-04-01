class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        middle = 0
        while(left <= right):
            middle = (left+right) // 2
            if(nums[middle] > target):
                right = middle - 1
            elif(nums[middle] < target):
                left = middle + 1
            else:
                return middle
        return left # i thought it would be return middle, but the last iteration will ruin the middle variable to be 0 if the ans is to be inserted at positon 1, but left will then become 1
    

sol = Solution()
nums = [1,3,5,6]
target = 2
sol.searchInsert(nums,target)