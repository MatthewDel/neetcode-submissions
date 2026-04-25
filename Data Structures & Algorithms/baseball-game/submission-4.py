class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Empty Record
        # Apply to the record operations 
            # Integer: record a new score
            # + - record a new score that is the sum of the previous two scores
            # 'D' - Record a new score double the previous one 
            # 'C' - Remove the record

        stack = []
        for action in operations:
            if action == "+":
                one = stack[-1]
                two = stack[-2]
                stack.append(one + two)
            elif action == "D":
                stack.append(stack[-1] * 2)
            elif action == "C":
                stack.pop()
            else:
                stack.append(int(action))
        
        sol = 0 
        while stack:
            sol += stack.pop()
        
        return sol
