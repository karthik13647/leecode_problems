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

        for i in range(val, n - 1):
            if nums[i] > nums[i+1]:
                return False

        if cnt == 1 and nums[-1] > nums[0]:
            return False
        return True
