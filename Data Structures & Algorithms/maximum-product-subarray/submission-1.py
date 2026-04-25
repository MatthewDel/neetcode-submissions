class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')

        for i in range(len(nums)):
            running = nums[i]
            max_product = max(running, max_product)
            for j in range(i + 1, len(nums)):
                running *= nums[j] 
                max_product = max(running, max_product)
        return max_product 