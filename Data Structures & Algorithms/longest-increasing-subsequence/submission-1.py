class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def helper(index, curr):
            nonlocal memo
            if (index, curr) in memo:
                return memo[(index, curr)]
            if index == len(nums):
                return 0
            
            sol = 0
            for i in range(index, len(nums)):
                if nums[i] > curr:
                    sol = max(sol, 1 + helper(i + 1, nums[i]))
            
            memo[(index, curr)] = sol 
            return sol
        
        return helper(0, float('-inf'))