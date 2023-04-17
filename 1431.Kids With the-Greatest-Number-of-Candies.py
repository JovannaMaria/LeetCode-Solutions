class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        op=[]
        for i in candies:
            x=i+extraCandies
            if max(candies)<=x:
                op.append(True)
            else:
                op.append(False)
        return op