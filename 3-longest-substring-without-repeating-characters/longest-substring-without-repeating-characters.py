class Solution:
    def lengthOfLongestSubstring(self,string1):
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(string1)):
            while string1[right] in seen:
                seen.remove(string1[left])
                left += 1
            seen.add(string1[right])
            max_len = max(max_len, right - left + 1)

        return max_len

        
