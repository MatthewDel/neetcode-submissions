class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        max_amount = nums[0]

        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            max_amount = max(max_amount, curr)
        return max_amount