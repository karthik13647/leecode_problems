class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #nums[:]=sorted(set(nums))
        a=[nums[0]]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                a.append(nums[i+1])
            if nums[i]==nums[i+1]:
                i+=1
        nums[:]=a
        
