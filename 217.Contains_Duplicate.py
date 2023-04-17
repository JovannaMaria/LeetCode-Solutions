class Solution(object):
    def containsDuplicate(self, nums):
        l=len(nums)
        ln=len(set(nums))
        if l>ln:
            return True
        else :
            return False