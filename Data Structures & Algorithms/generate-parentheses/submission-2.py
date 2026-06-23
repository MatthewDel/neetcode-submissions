class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []

        def helper(open_parentheses, closed_parentheses, temp):
            if closed_parentheses > open_parentheses or (open_parentheses) > ((n * 2) / 2):
                return
            
            if (open_parentheses) == ((n * 2) / 2) and (closed_parentheses) == ((n * 2) / 2):
                sol.append(''.join(temp))
                return
            
            temp.append("(")
            helper(open_parentheses + 1, closed_parentheses, temp)
            temp.pop()

            temp.append(")")
            helper(open_parentheses, closed_parentheses + 1, temp)
            temp.pop()

        helper(0, 0, [])
        return sol
