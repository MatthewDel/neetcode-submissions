class Solution:
    def helper(self, nums: List[int]) -> int:
        tabulation = [0] * (len(nums) + 3)
        for i in range(len(nums) - 1, -1, -1):
            tabulation[i] = nums[i] + max(tabulation[i+2], tabulation[i+3])
        return max(tabulation[0], tabulation[1])

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

