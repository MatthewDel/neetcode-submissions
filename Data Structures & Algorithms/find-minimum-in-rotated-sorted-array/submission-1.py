class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1 
        lowest_val = nums[0]
        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[left] <= nums[right]:
                return min(lowest_val, nums[left])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return lowest_val 

        
     
