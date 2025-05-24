class Solution:
    def check(self, nums) -> bool:
        val = 0
        cnt = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                val = i
                cnt += 1
        if cnt > 1:
            return False
        # Check if array is sorted from val to the end
        for i in range(val, n - 1):
            if nums[i] > nums[i+1]:
                return False
        # If rotated, last element should be <= first element
        if cnt == 1 and nums[-1] > nums[0]:
            return False
        return True
