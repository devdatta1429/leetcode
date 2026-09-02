class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dic = {}

        # Count characters in magazine
        for i in magazine:
            dic[i] = dic.get(i, 0) + 1

        # Use characters for ransomNote
        for i in ransomNote:
            if i not in dic or dic[i] == 0:
                return False

            dic[i] -= 1

        return True