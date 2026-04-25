class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(coins, amount):
            nonlocal memo 
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0 
            if amount < 0:
                return float('inf')
            res = float('inf')
            for coin in coins:
                res = min(res, 1 + helper(coins, amount - coin))
            memo[amount] = res
            return memo[amount]
        sol = helper(coins, amount)
        if sol == float('inf'):
            return -1 
        return sol 
            
        

        
