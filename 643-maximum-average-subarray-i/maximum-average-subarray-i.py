class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        z = window_sum

        for i in range((len(nums)- k)):
            window_sum = window_sum - nums[i] + nums [i+k] 

            if  window_sum > z:
                z = window_sum
        
        return float(z)/k