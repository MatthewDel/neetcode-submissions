class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set("+-*/")
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                first_value = stack.pop()
                second_value = stack.pop()

                if tokens[i] == '+':
                    stack.append(second_value + first_value)
                elif tokens[i] == '-':
                    stack.append(second_value - first_value)
                elif tokens[i] == '*':
                    stack.append(second_value * first_value)
                else:
                    stack.append(int(second_value / first_value))

        return stack[-1]
                