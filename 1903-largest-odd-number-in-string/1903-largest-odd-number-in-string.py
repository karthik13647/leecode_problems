class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)-1
        for i in range(n,-1,-1):
            k=int(num[i])
            if k%2!=0:
                return num[:i+1]
        return ""