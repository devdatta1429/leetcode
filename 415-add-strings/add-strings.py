class Solution(object):
    def addStrings(self, num1, num2):
        nums=[]
        carry=0

        i=len(num1)-1
        j=len(num2)-1

        while i>=0 or j>=0 or carry>0:

            if i>=0:
                carry+=int(num1[i])
                i-=1

            if j>=0:
                carry+=int(num2[j])
                j-=1

            nums.append(str(carry%10))
            carry= carry //10

        return ''.join(nums[::-1])