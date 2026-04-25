class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(step, memo):
            if step >= len(cost):
                return 0
            if step in memo:
                return memo[step]

            memo[step] = cost[step] + min(helper(step + 1, memo), helper(step + 2, memo))

            return memo[step]

        hash_map = {}
        return min(helper(0, hash_map), helper(1, hash_map))