class Solution(object):
    def search(self, nums, tgt):
        l=0
        r=len(nums)-1
        while r>=l:
            m=(l+r)//2
            if nums[m]==tgt:
                return m
            elif nums[m]>=nums[r]:
                if tgt>nums[m] or tgt<=nums[r]:
                    l=m+1
                else:
                    r=m-1
            else:
                if tgt<nums[l] or tgt>nums[m]:
                    l=m+1
                else:
                    r=m-1
        return -1
                    

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
     