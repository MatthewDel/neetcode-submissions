class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(step, memo):
            if step in memo:
                return memo[step]
            if step >= len(nums):
                return 0
            
            memo[step] = nums[step] + max(helper(step+2, memo), helper(step+3, memo))
            return memo[step]
        
        hash_map = {}
        return max(helper(0, hash_map), helper(1, hash_map))
        
        

        