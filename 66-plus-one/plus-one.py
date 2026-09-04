class Solution(object):
    def plusOne(self, digits):
        k=''

        for i in digits:
            k+=str(i)
        
        l=int(k)+1
        
        
        return [int(i) for i in str(l)]


        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] < 9:
        #         digits[i]+=1
        #         return digits
        #     else:
        #         digits[i]=0

        # return [1] + digits
        
        