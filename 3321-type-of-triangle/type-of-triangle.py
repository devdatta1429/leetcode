class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if ((nums[0]+nums[1])<=nums[2] or   # Python doesn't allow a line break 
                                            # after or unless you use one of these:
            (nums[1]+nums[2])<=nums[0] or   # 1. Parentheses (recommended)
            (nums[2]+nums[0])<=nums[1] ):   # 2. Backslash \
            return 'none'
        elif nums[0]==nums[1]==nums[2]:
            return 'equilateral'   
        elif (nums[0]+nums[1])>nums[2] and nums[0]==nums[1] or \
             (nums[1]+nums[2])>nums[0] and nums[1]==nums[2] or \
             (nums[2]+nums[0])>nums[1] and nums[2]==nums[0] :
            return 'isosceles'
        else:
            return 'scalene'