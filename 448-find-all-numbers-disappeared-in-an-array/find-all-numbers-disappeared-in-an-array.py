class Solution(object):
    def findDisappearedNumbers(self, nums):
        # asd=[]
        seen=set(nums)
        # for i in range(1,len(nums)+1):
        #     if i not in seen:
        #         asd.append(i)
        # return asd
         
        return [i for i in range(1,len(nums)+1) if i not in seen]