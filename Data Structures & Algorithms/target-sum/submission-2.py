class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def helper(index, running_sum):
            nonlocal memo
            if (index, running_sum) in memo:
                return memo[(index, running_sum)]
            if running_sum == target and index == len(nums):
                return 1
            if index == len(nums):
                return 0
            
            memo[(index, running_sum)] = helper(index + 1, running_sum + nums[index]) + helper(index + 1, running_sum - nums[index])
            return memo[(index, running_sum)]
        return helper(0, 0)