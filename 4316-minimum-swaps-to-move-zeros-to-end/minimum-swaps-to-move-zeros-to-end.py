class Solution(object):
    def minimumSwaps(self, nums):
        i=0
        l=0
        k=len(nums)-1

        while i< k:
            if nums[i]==0:
                if nums[k]!=0:
                    nums[k],nums[i]=nums[i],nums[k]
                    l+=1
                    i+=1
                    k-=1
                else:
                    k-=1
            else:
                i+=1
        return l