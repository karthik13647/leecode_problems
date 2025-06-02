class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        def lowerbound(nums,target):
            low=0
            high=len(nums)-1
            a=-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]>=target:
                    if nums[mid]==target:
                        a=mid
                    high=mid-1
                else:
                    low=mid+1
            return a
        
        def upperbound(nums,target):
            low=0
            high=len(nums)-1
            b=-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]<=target:
                    if nums[mid]==target:
                        b=mid
                    low=mid+1
                else:
                    high=mid-1
            return b
        
        a=lowerbound(nums,target)
        b=upperbound(nums,target)
        return [a,b]