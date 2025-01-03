class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p={}
        for key,ele in enumerate(nums):
            b=target-ele
            if b in p:
                return [p[b],key]
            p[ele]=key