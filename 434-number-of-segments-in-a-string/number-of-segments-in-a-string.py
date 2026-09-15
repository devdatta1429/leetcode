class Solution(object):
    def countSegments(self, s):
        # return len(list(s.split()))

        cnt=0
        for i in s.split():
            cnt+=1
        return cnt