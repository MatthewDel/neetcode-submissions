class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.sol = []
        def generateParentheses(stack, opens, close):
            if opens == 0 and close == 0:
                self.sol.append("".join(stack))
                return
            if opens > 0:
                stack.append("(")
                generateParentheses(stack, opens-1, close)
                stack.pop()
            if close > 0 and opens<close:
                stack.append(")")
                generateParentheses(stack,opens,close-1)
                stack.pop()
        generateParentheses([],n,n)
        return self.sol
