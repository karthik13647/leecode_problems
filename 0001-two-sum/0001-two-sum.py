class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,ele in enumerate(nums):
            val=target-ele
            if val in dic:
                return [dic[val],i]
            dic[ele]=i