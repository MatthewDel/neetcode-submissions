class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tabulation = [float('inf')] * (amount + 1)
        tabulation[0] = 1
        for i in range(amount):
            for coin in coins:
                if (i + coin) > amount:
                    continue 
                if tabulation[i + coin] != 0:
                   tabulation[i + coin] = min(tabulation[i] + 1, tabulation[i + coin])

        if tabulation[amount] == float('inf'):
            return -1 
        return tabulation[amount] - 1