class Solution:
    def countSubstrings(self, s: str) -> int:
        hashmap = {}
        count = 0
        def helper(i,j):
            nonlocal hashmap
            if s[i] == s[j]:
                if j - i <= 2 or helper(i + 1, j - 1):
                    hashmap[(i,j)] = True 
                    return True
                hashmap[(i,j)] = False
                return False 

        for i in range(len(s)):
            for j in range(i, len(s)):
                if helper(i,j):
                    count += 1
        
        return count


         
                