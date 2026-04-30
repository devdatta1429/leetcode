# class Solution:
#   def addBinary(self, a: str, b: str) -> str:
#     s = []
#     carry = 0
#     i = len(a) - 1
#     j = len(b) - 1

#     while i >= 0 or j >= 0 or carry:
#       if i >= 0:
#         carry += int(a[i])
#         i -= 1
#       if j >= 0:
#         carry += int(b[j])
#         j -= 1
#       s.append(str(carry % 2))
#       carry //= 2
#     return ''.join(reversed(s))
    


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        return( format( int(a,2)+int(b,2) , 'b' )) 
        
# #        a = int(a,2) 3 convert the string binary number to intger 
# #        b = int(b,2) 1 convert the string binary number to intger 
# #        c = a + b    4
# #        d = format(c,'b')   convert the number from  intger to binary number in string 
# #        return(d)

       

        
        
        