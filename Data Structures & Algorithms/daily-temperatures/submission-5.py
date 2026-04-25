class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        sol = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            temperature = temperatures[i]

            while stack and temperatures[stack[-1]] <= temperature:
                stack.pop()

            if not stack:
                sol[i] = 0
            else:
                sol[i] = stack[-1] - i

            stack.append(i)
        
        return sol

            

