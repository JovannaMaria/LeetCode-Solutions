class Solution(object):
    def productExceptSelf(self, nums):
        prev=1
        ans=[0]*len(nums)
        nextt=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            nextt[i]=nextt[i+1]*nums[i+1]
        for i in range(0,len(nums)):
            ans[i]=prev*nextt[i]
            prev=prev*nums[i]
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        