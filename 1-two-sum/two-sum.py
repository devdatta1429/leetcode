class Solution:
    def twoSum(self, nums, target):
        dic= {}
        for i in range(len(nums)):
            dic[nums[i]]= i
        
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in dic.keys() and i != dic[remain]:
                return dic[remain],i  