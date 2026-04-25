class Solution:
    def isValid(self, s: str) -> bool:
        hashset=set("[{(")
        stack = []
        for char in s:
            if char in hashset:
                stack.append(char)
            else:
                if stack == [] or (char == "]" and stack[-1] != "[") or (char == "}" and stack[-1] != "{") or (char == ")" and stack[-1] != "("):
                    return False 
                stack.pop()
        return stack == []