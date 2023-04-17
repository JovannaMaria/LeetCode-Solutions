class Solution(object):
    def romanToInt(self, s):
        result=0
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for a,b in zip(s,s[1:]):
            if roman[a]<roman[b]:
                result= result - roman[a]
            else :
                result= result + roman[a]
        return result + roman[s[-1]]