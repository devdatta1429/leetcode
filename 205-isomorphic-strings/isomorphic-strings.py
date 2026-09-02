class Solution(object):
    def isIsomorphic(self, s, t):
        dic={}
        used_j=set()
        for i,j in zip(s,t):
            if i not in dic:
                if j in used_j:
                    return False

                dic[i]=j
                used_j.add(j)
            else:
                if j!=dic[i]:
                    return False
        return True
