from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            
            # Check if the left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:  # Target in the left sorted part
                    high = mid - 1
                else:  # Target in the right unsorted part
                    low = mid + 1
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[high]:  # Target in the right sorted part
                    low = mid + 1
                else:  # Target in the left unsorted part
                    high = mid - 1
        
        return False
