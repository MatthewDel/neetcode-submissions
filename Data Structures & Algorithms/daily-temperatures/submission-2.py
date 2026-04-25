class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        sol = [0]  * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            while monotonic_stack and temperatures[i] >= temperatures[monotonic_stack[-1]]:
                monotonic_stack.pop()
            if monotonic_stack == []:
                sol[i] = 0
            else: 
                sol[i] = monotonic_stack[-1] - i
            
            monotonic_stack.append(i)
        return sol