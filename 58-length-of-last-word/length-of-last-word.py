class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip().split(" ")[-1]
        if type(s)==str: 
            return len(s) 

    
#    class Solution:
#    def lengthOfLastWord(self, s: str) -> int:
#        s = s.rstrip()  # s = "   fly me   to   the moon" only remove trailing spaces
#        return len(s) - s.rfind(' ') - 1
#                 25   -  22(where we find the space) -1 