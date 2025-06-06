class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        add=0
        for i in range(len(s)):
            if i<len(s)-1 and dic[s[i+1]]>dic[s[i]]:
                add-=dic[s[i]]
            else:
                add+=dic[s[i]]
            # print(add)
        return add