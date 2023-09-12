class Solution(object):
    def longestConsecutive(self, nums):
        nset=set(nums)
        longest=0
        for n in nset:
            if n-1 not in nset:
                length=1
                while n+length in nset:
                    length+=1
                longest=max(longest,length)
        return longest
        """
        :type nums: List[int]
        :rtype: int
        """
        