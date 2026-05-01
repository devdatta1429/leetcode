class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        cht = columnNumber
        while cht > 0:
            cht = cht-1

            ans += chr ( (cht%26) + ord("A") )

            cht = cht//26

        return ans[::-1]