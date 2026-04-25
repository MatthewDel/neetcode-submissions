class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        tabulation = [0] * len(cost)
        tabulation[len(cost) -1] = cost[len(cost) - 1] 
        tabulation[len(cost) -2] = cost[len(cost) - 2]
        for i in range(len(cost) - 3, -1, -1):
            tabulation[i] = cost[i] + min(tabulation[i + 1], tabulation[i + 2])
        return min(tabulation[0], tabulation[1])
