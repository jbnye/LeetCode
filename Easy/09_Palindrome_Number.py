class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        num = 0
        y = x
        while(y != 0):
            num = (num * 10) + (y%10)
            y = y // 10
        return (x == num)
        
print (3 // 2)    




# def isPalindrome(self, x):
    #     array = []
    #     y = x
    #     if(x < 0):
    #         return False
    #     while y != 0:
    #         array.append(y%10)
    #         y = (y / 10)
    #     left = 0
    #     right = len(array) - 1

    #     while left <= right:
    #         if(array[left] == array[right]):
    #             left += 1
    #             right -= 1
    #         else:
    #             return False
    #     return True