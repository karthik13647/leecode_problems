class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bal=0
        ele=0
        for i in nums:
            if bal==0:
                ele=i
            if ele==i:
                bal+=1
            else:
                bal-=1
        return ele        