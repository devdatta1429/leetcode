class Solution(object):
    def addDigits(self, num):
        while num>=10:
            total=0
            for i in str(num):
                total+=(int(i))
            num=total
        return num
        