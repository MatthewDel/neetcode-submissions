class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        left = 0
        right = 0 
        while right < len(prices):
            res = max(prices[right] - prices[left], res)
            if prices[left] > prices[right]:
                left = right 
            right += 1 
        return res