class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        op=0
        i=0
        t=0
        while(i<len(s)-1):
            if dic[s[i]]<dic[s[i+1]]:
                op-=dic[s[i]]
            else:
                op+=dic[s[i]]            
            i+=1
        op+=dic[s[-1]]
        return op