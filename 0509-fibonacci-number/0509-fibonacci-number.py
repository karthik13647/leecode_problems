class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        a=[0,1]
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
        return a[-1]
        # if n==0:
        #     return 0
        # if n==1 or n==2:
        #     return 1
        # else:
        #     return self.fib(n-1)+self.fib(n-2)