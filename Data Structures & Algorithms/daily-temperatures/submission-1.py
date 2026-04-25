class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            curr = temperatures[i]
            while stack and curr >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            else:
                res[i] = 0
            stack.append(i)

        return res