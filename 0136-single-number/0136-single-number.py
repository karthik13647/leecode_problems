class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for ele in nums:
            x=x^ele
        return x