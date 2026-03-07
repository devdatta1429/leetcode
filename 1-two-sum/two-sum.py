class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i in range(0,len(nums)):
            dic[nums[i]]=i

        i=0
        while i < len(nums):
            remain=target-nums[i]
            if remain in dic and dic[remain]!=i:
                return dic[remain],i
            # dic[nums[i]]= i
            i+=1

        