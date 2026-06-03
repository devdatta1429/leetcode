class Solution:
    def twoSum(self, nums, target):
        dic = {}

        for i , num in enumerate(nums):
            remain = target - num
            if remain in dic:
                return dic[remain],i
            
            dic[num] = i  
