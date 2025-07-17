from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        l=[]
        for key,ele in c.items():
            if ele==1:
                l.append(key)
        return l