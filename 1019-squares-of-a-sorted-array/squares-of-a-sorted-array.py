class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)

        Why?
        lst = [0] * n → O(n) time and O(n) space.
        Two-pointer while loop → runs at most n times, so O(n).
        lst[k] = value → O(1) per assignment."""

        n = len(nums)
        lst=[0]*n

        a = 0
        b = n-1
        k = n-1

        while a<=b:
            if nums[a]**2<nums[b]**2:
                lst[k] = nums[b]**2
                b-=1
            else:
                lst[k] = nums[a]**2
                a+=1
            k-=1
        return lst


    """Time Complexity: O(n²)
        Space Complexity: O(n)

        Why O(n²)?

        The while loop runs O(n) times.
        insert(0, value) takes O(n) because existing elements need to shift right.
        Therefore, O(n) × O(n) = O(n²)"""

        # lst=[]
        # a=0
        # b=len(nums)-1
        # while a<=b:
        #     if nums[a]**2<nums[b]**2:
        #         lst.insert(0,nums[b]**2)
        #         b-=1
        #     else:
        #         lst.insert(0,nums[a]**2)
        #         a+=1
        # return lst