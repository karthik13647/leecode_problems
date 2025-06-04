class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        a=[]
        bal=0
        for ele in s:
            if ele=='(':
                if bal>0:
                    a.append(ele)
                bal+=1
            elif ele==')':
                bal-=1
                if bal>0:
                    a.append(ele)

        return ''.join(a)