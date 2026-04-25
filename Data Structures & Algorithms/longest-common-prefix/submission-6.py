class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol = strs[0]

        for i in range(1, len(strs)):
            index = 0

            while index < min(len(sol), len(strs[i])):
                if sol[index] != strs[i][index]:
                    break 
                index += 1
            
            sol = sol[:index]
        
        return sol 