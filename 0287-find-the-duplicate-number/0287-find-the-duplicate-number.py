#from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Method 1
        # k=Counter(nums)
        # max_ele=None
        # m=float('-inf')
        # for ele,freq in k.items():
        #     if m<freq:
        #         m=freq
        #         max_ele=ele
        # return max_ele

        #Method 2
        # k=set()
        # for ele in nums:
        #     if ele in k:
        #         return ele
        #     k.add(ele)

        # method 1 & 2 both takes the time complexity of O(N) and space complexity of O(N)

        # Method 3 (Optimal with time and space complexity of O(N) and O(1))
        slow=fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow=nums[0]
        while(slow!=fast):
            slow=nums[slow]
            fast=nums[fast]
        return slow