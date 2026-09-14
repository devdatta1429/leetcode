class Solution(object):
    def longestPalindrome(self, s):
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i] = (dic[i] + 1)
        
        z=0
        max_odd=0
        for i in dic:
            if dic[i]%2==0:
                z+=dic[i]
            else:                
                max_odd = 1
                z+=(dic[i]-1)
        
        return z + max_odd
