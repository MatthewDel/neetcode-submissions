class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(coins, amount,memo):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0 
            elif amount < 0:
                return float('inf')
            ans = float('inf')
            for coin in coins:
                ans = min(ans, helper(coins, amount - coin,memo))
            memo[amount] = 1 + ans 
            return memo[amount]
        result = helper(coins, amount,{}) 
        if result == float('inf'):
            return -1
        else:
            return result