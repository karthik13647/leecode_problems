class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        k=[]
        for i in range(numRows):
            if i==0:
                l.append([1])
            elif i==1:
                l.append([1,1])
            else:
                a=l[-1]
                k=[1]
                for j in range(len(a)-1):
                    k.append(a[j]+a[j+1])
                k.append(1)
                l.append(k)
        return l