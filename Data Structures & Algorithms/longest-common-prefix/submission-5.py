class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol = strs[0]
        for i in range(1,len(strs)):
            if not sol or not strs[i]:
                return ""
            for j in range(min(len(sol),len(strs[i]))):
                if sol[j] != strs[i][j]:
                    sol = sol[:j]
                    break
                if j == len(strs[i]) - 1:
                    sol = sol[:j+1]
        return sol