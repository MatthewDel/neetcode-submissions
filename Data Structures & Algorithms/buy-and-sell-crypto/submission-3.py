class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_output = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                max_output = max(max_output, prices[j] - prices[i])
        return max_output