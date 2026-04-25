class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1 

        while left <= right:
            
            while left <= right and nums[right] == val:
                right -= 1

            while left <= right and nums[left] != val:
                left += 1

            if left > right:
                return left
            
            nums[left] = nums[right] 
            nums[right] = val

        
        return left