class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        runningAnd = nums[0]
        for i in range(1, len(nums)):
            runningAnd ^= nums[i]
        
        return runningAnd