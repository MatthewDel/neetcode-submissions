class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1 
        tabulation = [0] * (n + 1)
        tabulation[1] = 1
        tabulation[2] = 1 

        for i in range(3, len(tabulation)):
            tabulation[i] = tabulation[i-3] + tabulation[i-2] + tabulation[i-1]
        return tabulation[len(tabulation) - 1]