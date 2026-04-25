class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def helper(indexOne, indexTwo):

            if (indexOne, indexTwo) in memo:
                return memo[(indexOne, indexTwo)]

            if indexOne == len(text1) or indexTwo == len(text2):
                return 0

            if text1[indexOne] == text2[indexTwo]:
                memo[(indexOne, indexTwo)] = 1 + helper(indexOne + 1, indexTwo + 1)
            else:
                memo[(indexOne, indexTwo)] = max(helper(indexOne+1, indexTwo), helper(indexOne, indexTwo+1))
            
            return memo[(indexOne, indexTwo)]
        
        return helper(0,0)
        