class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        for ele in nums:
            if nums.count(ele)>2:
                return False
                # print(nums.count(ele))
        return True
