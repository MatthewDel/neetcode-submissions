class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []

        intervals.sort()

        sol.append(intervals[0])

        for i in range(len(intervals)):
            temp = intervals[i]
            if sol[-1][1] < temp[0]:
                sol.append(temp)
            else:
                sol[-1][1] = max(sol[-1][1], temp[1])
            
        return sol 