class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        memo = {}
        def helper(index):
            nonlocal memo
            if index in memo:
                return memo[index]

            if index == len(s):
                return True 
            
            sol = False 
            for word in wordDict:
                if ((index + len(word)) <= len(s)) and s[index: index + len(word)] == word:
                    if helper(index + len(word)):
                        memo[index] = True 
                        return memo[index]

            memo[index] = False  
            return memo[index]
        
        return helper(0)

            
