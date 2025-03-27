class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        middle = 0
        while left <= right:
            middle = (left + right) // 2
            if(nums[middle] == target):
                return middle
            elif(nums[middle] < target):
                left = middle + 1
            else:
                right = middle - 1
        return -1 
        