class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        i,j=0,0
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]]!=t[i]:
                    return False
            else:  
                dic[s[i]]=t[i]
        k1=len(set(s)) and len(set(t))
        k2=len(dic)==len(set(t))
        return k1 and k2