class Solution(object):
    def isSubsequence(self, s, t):
        # k = ""
        # z=len(s)+1
        # r=s[-z:]
        # for i in t:
        #     if z>0:
        #         if i in s:
        #             k+=i
        #             z-=1
        # if k==s:
        #     return True
        # else:
        #     return False

   
        j = 0

        for i in t:
            if j < len(s) and i == s[j]:
                j += 1

        return j == len(s)
