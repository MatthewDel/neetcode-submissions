class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]

        left = 0
        right = len(intervals) - 1 
        target = newInterval[0]
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        intervals.insert(left, newInterval)
        print(intervals)
        sol = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > sol[-1][1]:
                sol.append(intervals[i])
            else:
                sol[-1][1] = max(sol[-1][1],intervals[i][1])
        return sol
                
            