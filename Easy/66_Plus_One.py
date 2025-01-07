class Solution(object):
    def plusOne(self, digits):
        carry = False
        for x in range(len(digits) - 1, -1, -1):
            digits[x] += 1
            if(digits[x] != 10):
                return digits
            if(digits[x] == 10):
                digits[x] = 0
            if(x == 0):
                digits[x] = 1
                digits.append(0)
        return digits