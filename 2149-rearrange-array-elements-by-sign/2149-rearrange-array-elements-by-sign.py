class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        res=[]
        for ele in nums:
            if ele>0:
                a.append(ele)
            else:
                b.append(ele)
        for j in range(len(nums)//2):
            res.append(a[j])
            res.append(b[j])
        return res
        