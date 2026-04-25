class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums) - 1 
        left = 0
        for i in range(len(nums)):
            if nums[left] == val:
                nums[left] = nums[right]
                nums[right] = val
                right -= 1
            else:
                left += 1
        
        return left 
            