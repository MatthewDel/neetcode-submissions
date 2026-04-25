class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def helper(index):
            nonlocal memo 

            if index == len(s):
                return 1
            if index in memo:
                return memo[index]
            if(s[index] == '0'):
                return 0
            
            res = helper(index + 1)

            if index + 1 < len(s) and (10 <= int(s[index:index+2]) <= 26):
                res += helper(index + 2)
            
            memo[index] = res
            return res 
        
        return helper(0)
            