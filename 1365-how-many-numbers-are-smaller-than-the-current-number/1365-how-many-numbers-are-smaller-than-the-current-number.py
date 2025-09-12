class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=sorted(nums)
        d={}
        for i,num in enumerate(l):
            if num not in d:
                d[num]=i
        res=[]
        for ele in nums:
            res.append(d[ele])
        return res