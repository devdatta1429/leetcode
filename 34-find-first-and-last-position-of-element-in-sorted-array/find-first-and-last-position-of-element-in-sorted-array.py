# class Solution(object):
#     def searchRange(self, nums, target):
#         lst=[]
#         k=0
#         while k =< (len(nums)//2)+1:
#             if nums[k]==target:
#                 if len(lst)<1:
#                     lst.append(k)
#                 else:
#                     lst.insert(0,k)
#             if nums[-(k+1)]==target:
#                 lst.append(k)
#             k+=1
#         if len(lst)<1:
#             return [-1,-1]
#         else:
#             return lst

class Solution(object):
    def searchRange(self, nums, target):

        left = 0
        right = len(nums) - 1
        first = -1

        # Find first occurrence
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1
        last = -1

        # Find last occurrence
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [first, last]