class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(step):
            if step >= len(cost):
                return 0
            return cost[step] + min(helper(step + 1), helper(step + 2))
        
        return min(helper(0), helper(1))