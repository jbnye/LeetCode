class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for x in range(len(flowerbed)):
            prev = (x == 0) or (flowerbed[x-1] == 0)
            next = (x == len(flowerbed) -1) or (flowerbed[x+1] == 0)

            if(prev == True) and (next == True) and (flowerbed[x] == 0):
                flowerbed[x] = 1
                count += 1
        if(count >= n):
            return True
        return False