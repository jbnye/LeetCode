class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num 
            elif num <= second:
                second = num 
            else:
                return True  
        
        return False