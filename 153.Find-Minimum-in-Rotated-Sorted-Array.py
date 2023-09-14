class Solution(object):
    def findMin(self, nums):
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r-1)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        return nums[l]