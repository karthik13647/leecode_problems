class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ele in tokens:
            if ele in "+-*/":
                b,a=stack.pop(),stack.pop()
                if ele=="+":
                    stack.append(a+b)
                if ele=="*":
                    stack.append(a*b)
                if ele=="-":
                    stack.append(a-b)
                if ele=="/":
                    res=int(a/b)
                    if res<0:
                        stack.append(ceil(res))
                    else:
                        stack.append(res)
            else:
                stack.append(int(ele))
        return stack[-1]