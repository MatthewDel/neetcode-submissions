class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for car in (sorted(arr)[::-1]):
            stack.append((target-car[0])/car[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)