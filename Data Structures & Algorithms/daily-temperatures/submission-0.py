class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        sol = [0] * n 
        monotonic_stack = []
        monotonic_stack.append(n-1)
        for i in range(n-2, -1, -1):
            print(monotonic_stack)
            
            while monotonic_stack != [] and temperatures[i] >= temperatures[monotonic_stack[-1]]:
                monotonic_stack.pop()
            
            if monotonic_stack == []:
                sol[i] = 0
            else:
                count = monotonic_stack[-1] - i
                sol[i] = count
            monotonic_stack.append(i)
            
        return sol 
            
