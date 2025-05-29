class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        add=0
        for ele in nums:
            add+=ele
            if add>maxi:
                maxi=add
            if add<0:
                add=0
        return maxi
