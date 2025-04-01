class Solution(object):
    def isPalindrome(self, x):
        array = []
        y = x
        if(x < 0):
            return False
        while y != 0:
            array.append(y%10)
            y = (y / 10)
        left = 0
        right = len(array) - 1

        while left <= right:
            if(array[left] == array[right]):
                left += 1
                right -= 1
            else:
                return False
        return True
        
print (3 // 2)