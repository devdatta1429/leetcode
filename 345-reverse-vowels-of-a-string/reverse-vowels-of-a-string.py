class Solution(object):
    def reverseVowels(self, s):
        # lst=[]

        # for i in s:
        #     if i in "AEIOUaeiou":
        #         lst.append(i)
        
        # cnt=len(lst)-1
        # s = list(s)
        # for i in range(len(s)):
        #     if s[i] in "AEIOUaeiou":
        #         s[i]=lst[cnt]
        #         cnt-=1
        
        # return ''.join(s)
        
        s=list(s)
        vowels='AEIOUaeiou'

        left=0
        right=len(s) - 1

        while left < right:
            while left < right and s[left] not in vowels:
                left+=1
            
            while left < right and s[right] not in vowels:
                right-=1

            s[left],s[right]=s[right],s[left]

            left+=1
            right-=1

        return ''.join(s)