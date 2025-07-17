from collections import Counter 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        for key,ele in cnt.items():
            if ele==1:
                return key