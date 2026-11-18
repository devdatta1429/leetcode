class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dic={}

        for i in nums1:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        lst=[]
        for j in nums2:
            if j in dic and dic[j] > 0:
                lst.append(j)
                dic[j]-=1
        return lst





        """
        Time: O(n × m)
        Space: O(min(n, m)) for the result in the worst case."""
        """asd = []
        for i in nums2:
            if i in nums1:
                asd.append(i)
                nums1.remove(i)
        return asd
        """