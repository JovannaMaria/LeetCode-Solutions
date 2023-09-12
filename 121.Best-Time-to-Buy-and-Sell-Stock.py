class Solution(object):
    def maxProfit(self, prices):
        maxp=0
        low=prices[0]
        for i in prices[1:]:
            if i<low:
                low=i
            elif  maxp< i-low:
                maxp=i-low
        return maxp
        """
        :type prices: List[int]
        :rtype: int
        """