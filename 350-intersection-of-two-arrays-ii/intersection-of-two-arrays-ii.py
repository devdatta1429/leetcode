class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        asd = []
        for i in nums2:
            if i in nums1:
                asd.append(i)
                nums1.remove(i)
        return asd
        