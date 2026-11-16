class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        a = nums[0]
        b = nums[0]

        ind1=0
        ind2=1

        lst=[]
        while ind2 < len(nums):
            if nums[ind1]+1==nums[ind2]:
                b = nums[ind2] 
            else:
                if a==b:
                    lst.append(str(a))
                else:
                    lst.append(f'{a}->{b}')
                a = nums[ind2]
                b = nums[ind2]
            ind1+=1
            ind2+=1

        if a==b:
            lst.append(f'{a}')
        else:
            lst.append(f'{a}->{b}')
            
        return lst