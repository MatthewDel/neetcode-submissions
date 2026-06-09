class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(index, xor_sum):
            if index >= len(nums):
                return xor_sum
            
            return helper(index + 1, xor_sum) + helper(index + 1, xor_sum ^ nums[index])
        return helper(0,0)