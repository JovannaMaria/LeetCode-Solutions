class Solution(object):
    def longestCommonPrefix(self, strs):
        k=len(min(strs, key=len))
        flag=0
        while flag==0:
            flag=1
            for j in strs:
                if strs[0][:k]!=j[:k]:
                    k-=1
                    flag=0

        return strs[0][:k]
