class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        dic={}
        for i in range(26):
            dic[i]=chr(ord('z') - i)
        
        lst= ''
        a = 0
        for word in words:
            total = 0

            for char in word:
                total+= weights[ord(char)-ord('a')]
            
            rem = total%26
            lst+= dic[rem]

        return lst


