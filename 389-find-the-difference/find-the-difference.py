class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        remain=0
        for i in t+s:
            remain ^= ord(i)
        return chr(remain)
        