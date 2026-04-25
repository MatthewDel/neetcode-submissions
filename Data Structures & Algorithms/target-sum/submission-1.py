class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    
        def helper(index, running_sum):
            if running_sum == target and index == len(nums):
                return 1
            if index == len(nums):
                return 0
            
            return helper(index + 1, running_sum + nums[index]) + helper(index + 1, running_sum - nums[index])
        return helper(0, 0)