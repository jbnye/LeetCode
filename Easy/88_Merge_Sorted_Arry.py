class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if(n == 0):
            return nums1
        if(m == 0):
            return nums2
        p1 = 0
        p2 = 0
        ans = []
        while(p1 != n or p2 != n):
            if(p1 == (n)):
                ans.append(nums2[p2])
                p2 += 1
            elif(p2 == n):
                ans.append(nums1[1])
                p1 += 1
            elif(nums1[p1] <= nums2[p2]):
                ans.append(nums1[p1])
                p1 += 1
            else:
                ans.append(nums2[p2])
                p2 += 1
        return ans