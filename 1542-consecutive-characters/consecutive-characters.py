class Solution(object):
    def maxPower(self, s):
        k=1
        j=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                j+=1
            else:
                j=1
            
            if k<j:
                k=j
        return k