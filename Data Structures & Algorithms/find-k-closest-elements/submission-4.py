from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        running_sol = deque()

        for num in arr:
            if len(running_sol) < k:
                running_sol.append(num)
            else:
                left_dist = abs(running_sol[0] - x)
                new_dist = abs(num - x)

                if left_dist > new_dist:
                    running_sol.popleft()
                    running_sol.append(num)
                elif num > x:
                    break

        return list(running_sol)