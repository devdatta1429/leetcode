class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if type(s.strip().split(" ")[-1])==str: 
            return len(s.strip().split()[-1]) 

    
#    class Solution:
#    def lengthOfLastWord(self, s: str) -> int:
#        s = s.rstrip()  # s = "   fly me   to   the moon" only remove trailing spaces
#        return len(s) - s.rfind(' ') - 1
#                 25   -  22(where we find the space) -1 