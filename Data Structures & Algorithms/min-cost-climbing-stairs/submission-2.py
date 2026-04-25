class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(cost, index):
            if index >= len(cost):
                return 0
            return cost[index] + min(helper(cost, index + 1), helper(cost, index + 2))
        return min(helper(cost, 0), helper(cost, 1))

