class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        lst=[]
        a=0
        b=len(nums)-1
        while a<=b:
            if nums[a]**2<nums[b]**2:
                lst.insert(0,nums[b]**2)
                b-=1
            else:
                lst.insert(0,nums[a]**2)
                a+=1
        return lst