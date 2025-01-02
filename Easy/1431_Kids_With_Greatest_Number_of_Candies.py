class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        greatest = candies[0]
        ans = []
        if(candies):
            for x in range(len(candies)):
                if(greatest < candies[x]):
                    greatest = candies[x]
            for x in range(len(candies)):
                if (candies[x] + extraCandies >= greatest):
                    ans.append(True)
                else:
                    ans.append(False)
        return ans