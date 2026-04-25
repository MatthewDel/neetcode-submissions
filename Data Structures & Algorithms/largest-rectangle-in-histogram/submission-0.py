class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0],0)]

        max_value = 0

        for i in range(1, len(heights)):
            lastPop = -1 
            while stack and heights[i] < stack[-1][0]:
                top = stack.pop()
                max_value = max(max_value, top[0] * (i-top[1]))
                lastPop = top[1]
            if stack and heights[i] == stack[-1][0]:
                continue 
            elif not stack or heights[i] > stack[-1][0]:
                if lastPop != -1:
                    stack.append((heights[i], lastPop))
                else:
                    stack.append((heights[i], i))
            print(stack, max_value)
        
        while stack:
            top = stack.pop()
            max_value = max(max_value, top[0] * (len(heights)-top[1]))
            print(top,max_value)

        return max_value



