class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif stack==[] or (stack[-1] == "(" and s[i]!=")") or (stack[-1] == "{" and s[i]!="}") or (stack[-1] == "[" and s[i]!="]"):
                return False
            else:
                stack.pop()
                
        return stack == []