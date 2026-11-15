class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen={}

        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
            seen[nums[i]]=i
        return False


        """ Time Limit Exceeded """
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j] and j-i <= k:
        #             return True
        # return False
        