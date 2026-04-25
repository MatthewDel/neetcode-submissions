class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        left = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                temp = nums[left]
                nums[left] = 0
                nums[i] = temp
                left += 1
                
            elif nums[i] == 2:
                temp = nums[right] 
                nums[right] = 2
                nums[i] = temp 
                right -= 1
                i -= 1
            
            i += 1
        
        return nums
        
        