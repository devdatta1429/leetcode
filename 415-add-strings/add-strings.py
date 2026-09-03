class Solution(object):
    def addStrings(self, num1, num2):
        nums=[]
        carry=0

        len1=len(num1)-1
        len2=len(num2)-1

        while len1>=0 or len2>=0 or carry:

            if len1>=0:
                carry+=int(num1[len1])
                len1-=1

            if len2>=0:
                carry+=int(num2[len2])
                len2-=1

            nums.append(str(carry%10))
            carry= carry //10

        return str(''.join(nums[::-1]))