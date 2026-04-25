class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        stack = []
        def helper(opens, closed):
            if opens == closed == n:
                sol.append("".join(stack))
            if opens<n:
                stack.append("(")
                helper(opens + 1, closed)
                stack.pop()
            if closed<opens:
                stack.append(")")
                helper(opens, closed + 1)
                stack.pop()
        helper(0, 0)
        return sol