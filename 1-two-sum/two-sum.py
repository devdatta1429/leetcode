class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            remain= target-nums[i]
            if remain in dic.keys():
                return dic[remain],i
            dic[nums[i]] = i