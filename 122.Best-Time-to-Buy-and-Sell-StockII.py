class Solution(object):
    def maxProfit(self, prices):
        maxp=0
        low=prices[0]
        for i in prices[1:]:
            if low>i:
                low=i
            elif i-low>0 :
                maxp=i-low+maxp
                low=i
        return maxp
        """
        :type prices: List[int]
        :rtype: int
        """