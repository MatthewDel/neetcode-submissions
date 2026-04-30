class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p,s) for p, s in zip(position, speed)]
        arr.sort()
        stack = []

        for i in range(len(arr) - 1, -1, -1):
            time_to_target = (target - arr[i][0]) / arr[i][1]

            stack.append(time_to_target)

            if len(stack) >= 2 and stack[-1] <= stack [-2]:
                stack.pop()
            
        return len(stack)
    
        
