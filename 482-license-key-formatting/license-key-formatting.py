class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-" , "").upper()

        lst=[]
        cnt=0

        for i in range(len(s)-1 , -1 , -1):
            lst.append(s[i])
            cnt+=1

            if cnt==k:
                lst.append("-")
                cnt=0
        
        
        result = lst[::-1]

        if result and result[0] == "-":
            result.pop(0)
        

        return ''.join(result)


# class Solution(object):
#     def licenseKeyFormatting(self, s, k):
#         s = s.replace("-", "").upper()

#         result = []
#         count = 0

#         for i in range(len(s) - 1, -1, -1):
#             result.append(s[i])
#             count += 1

#             if count == k:
#                 result.append("-")
#                 count = 0

#         result = result[::-1]

#         if result and result[0] == "-":
#             result.pop(0)

#         return ''.join(result)