class Solution(object):
    def isSubsequence(self, s, t):
        k = ""
        z = 0
        
        for i in t:
            if z < len(s):
                if i==s[z]:
                    k+=i
                    z+=1
        if k==s:
            return True
        else:
            return False

   
        # j = 0

        # for i in t:
        #     if j < len(s) and i == s[j]:
        #         j += 1

        # return j == len(s)
