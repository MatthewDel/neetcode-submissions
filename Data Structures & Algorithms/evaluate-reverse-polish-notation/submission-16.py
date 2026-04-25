class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set("+-*/")

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                operator_two = int(stack.pop())
                operator_one = int(stack.pop())

                if token == '+':
                    stack.append(operator_one + operator_two)
                elif token == '-':
                    stack.append(operator_one - operator_two)
                elif token == '*':
                    stack.append(operator_one * operator_two)
                else:
                    stack.append(int(operator_one / operator_two))
        
        return int(stack[-1])

            

                