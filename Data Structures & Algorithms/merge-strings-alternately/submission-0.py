class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = []

        one = 0

        while one < len(word1) and one < len(word2):
            sol.append(word1[one])
            sol.append(word2[one])
            one += 1
        
        if one < len(word1):
            sol.append(word1[one:])
        if one < len(word2):
            sol.append(word2[one:])
        return ''.join(sol)
        