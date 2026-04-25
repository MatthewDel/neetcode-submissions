class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        def helper(cost, index):
            nonlocal memo
            if index >= len(cost):
                return 0
            if memo[index] != -1:
                return memo[index]
            memo[index] = cost[index] + min(helper(cost, index + 1), helper(cost, index + 2))
            return memo[index]
        return min(helper(cost, 0), helper(cost, 1))

