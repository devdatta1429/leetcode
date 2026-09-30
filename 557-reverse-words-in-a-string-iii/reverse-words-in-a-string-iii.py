class Solution(object):
    def reverseWords(self, s):
        k=[]
        for i in s.split():
            k.append(i[::-1])
        return str(' '.join(k))


        