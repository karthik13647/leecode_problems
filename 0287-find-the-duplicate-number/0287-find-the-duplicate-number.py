#from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # k=Counter(nums)
        # max_ele=None
        # m=float('-inf')
        # for ele,freq in k.items():
        #     if m<freq:
        #         m=freq
        #         max_ele=ele
        # return max_ele
        k=set()
        for ele in nums:
            if ele in k:
                return ele
            k.add(ele)