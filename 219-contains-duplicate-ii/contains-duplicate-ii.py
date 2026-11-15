class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen={}

        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
            seen[nums[i]]=i
        return False
        # Time Complexity: O(n) – One traversal of the array.
        # Space Complexity: O(n) – Dictionary stores elements.

        """ 
        Time Limit Exceeded 
        Time Complexity: O(n²)
        Space Complexity: O(1)"""
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j] and j-i <= k:
        #             return True
        # return False
        