class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        i = 1
        max_profit = 0
        while i < len(prices):
            max_profit = max(prices[i] - prices[left], max_profit)
            if prices[i] < prices[left]:
                left = i 
            i += 1
        return max_profit
