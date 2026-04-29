class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip().split(" ")[-1]
        if type(s)==str: 
            return len(s) 