class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        asd = set()
        for i in nums2:
            if i in nums1:
                asd.add(i)
        return list(asd)
        
        