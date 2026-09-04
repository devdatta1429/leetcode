class Solution(object):
    def firstUniqChar(self, s):
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
        
        for j in range(0,len(s)):
            if dic[s[j]]==1:
                return j
        return -1