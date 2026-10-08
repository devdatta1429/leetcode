class Solution(object):
    def thirdMax(self, nums):
        nums=list(set(nums))

        f_max = s_max = t_max = None


        for i in nums:
            if f_max is None or f_max < i :
                t_max = s_max
                s_max = f_max
                f_max = i
            else:
                if s_max < i:
                    t_max = s_max
                    s_max = i
                elif t_max < i :
                    t_max = i
            
       
        if len(nums)<3:
            return f_max
        else:
            return t_max