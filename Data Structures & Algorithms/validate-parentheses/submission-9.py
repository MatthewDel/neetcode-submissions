class Solution:
    def isValid(self, s: str) -> bool:
        lifo = []
        openers = set("[{(")
        for char in s:
            if char in openers:
                lifo.append(char)
            elif not lifo or not self.matching(lifo.pop(), char):
                return False
        return not lifo

    def matching(self, opener:char, closer:char) -> bool:
        if (opener == "(" and closer != ")") or (opener == "[" and closer != "]") or (opener == "{" and closer != "}"):
            return False
        return True