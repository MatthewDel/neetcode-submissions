class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(cost, index, memo):
            if index in memo:
                return memo[index]
            if index >= len(cost):
                return 0
            return cost[index] + min(helper(cost, index + 1, memo), helper(cost, index + 2, memo))
        return min(helper(cost, 0, {}), helper(cost, 1, {}))

