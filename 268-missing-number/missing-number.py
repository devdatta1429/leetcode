class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        actual_total= (len(nums) * (len(nums)+1)) // 2
        total = sum(nums)
        return (actual_total - total )

        