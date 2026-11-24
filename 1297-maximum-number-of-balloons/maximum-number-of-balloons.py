class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic={}
        for i in text:
            if i in "balon":
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
        
        # for i in 'balon':
        #     if i not in dic:
        #         return 0
        if len(dic)!=5:
            return 0
        a=0
        while 1<=dic['b']:
            if dic['b']>=1 and dic['a']>=1 and dic["l"]>=2 and dic['o']>=2 and dic['n']>=1:
                a+=1
                dic['b']-=1 
                dic['a']-=1
                dic['l']-=2
                dic['o']-=2
                dic['n']-=1
            else:
                return a
    
        return a