class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l=[]
        for ele in s:
            if ele in l:
                return ele
            else:
                l.append(ele)
        