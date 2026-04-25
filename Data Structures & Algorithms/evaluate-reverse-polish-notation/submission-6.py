class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                one = stack.pop()
                two = stack.pop()
                if tokens[i] == "+":
                    stack.append(one+two)
                elif tokens[i] == "-":
                    stack.append(two-one)
                elif tokens[i] == "*":
                    stack.append(one*two)
                else:
                    stack.append(int(two/one))
            else:
                stack.append(int(tokens[i]))
        return stack[0]