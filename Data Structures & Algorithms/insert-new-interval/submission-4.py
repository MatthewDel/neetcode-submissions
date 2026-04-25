class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]

        left = 0
        right = len(intervals) - 1 

        while left <= right:
            mid = (left + right) // 2 
            if intervals[mid][0] < newInterval[0]:
                left += 1
            else:
                right -= 1
        
        intervals.insert(left, newInterval)
        
        sol = [intervals[0]]

        for i in range(1, len(intervals)):
            temp = intervals[i]

            if sol[-1][1] < temp[0]:
                sol.append(temp)
            else:
                sol[-1][1] = max(sol[-1][1], temp[1])

            
        return sol
            

