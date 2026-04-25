class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                one = stack.pop()
                two = stack.pop()
                
                if token == "+":
                    stack.append(two + one)
                elif token == "-":
                    stack.append(two - one)
                elif token == "*":
                    stack.append(two * one)
                else: 
                    stack.append(int(two / one))

        return stack[-1]
