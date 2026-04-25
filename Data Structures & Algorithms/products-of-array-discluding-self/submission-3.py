class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        left = 1 
        for i in range(len(nums)):
            sol[i] = left 
            left = left * nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            sol[i] = sol[i] * right
            right = nums[i] * right
        
        return sol 
