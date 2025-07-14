class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        n=len(nums)
        for i in range(1,n+1):
            l.append(i)
        x=list(set(nums))
        n1=len(x)
        for i in range(n1):
            l.remove(x[i])
        return l

        # k=set(nums)
        # for i in range(1,max(nums)+1):
        #     if i not in nums:
        #         l.append(i)
        # if len(l)==0:
        #     if len(k)==len(nums):
        #         return []
        #     l.append(max(nums)+1)
        # return l