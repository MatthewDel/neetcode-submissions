class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[-1]
        second = cost[-2]

        if len(cost) <= 2:
            return min(first, second)

        for i in range(len(cost) - 3, -1, -1):
            temp = cost[i] + min(first, second)
            first = second
            second = temp
        
        return min(first, second)