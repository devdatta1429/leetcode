class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        a = 0
        b = len(numbers)-1

        while a<b:
            total = numbers[a]+numbers[b]

            if total==target:
                return a+1,b+1
            elif total<target:
                a+=1
            elif total > target:
                b-=1
        