class Solution(object):
    def reverseVowels(self, s):
        lst=[]

        for i in s:
            if i in "AEIOUaeiou":
                lst.append(i)
        
        cnt=len(lst)-1
        s = list(s)
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                s[i]=lst[cnt]
                cnt-=1
        
        return ''.join(s)
        