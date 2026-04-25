class Solution:
    def tribonacci(self, n: int) -> int:
        def memo(n, mem):
            if n in mem:
                return mem[n]
            if n == 0: 
                return 0
            elif n == 1 or n == 2:
                return 1 

            mem[n] = memo(n - 3, mem) + memo(n - 2, mem) + memo(n - 1, mem)
            return mem[n]
        return memo(n, {})