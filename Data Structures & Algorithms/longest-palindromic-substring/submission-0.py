class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Recurrence if i == j and (i - j <= 2 or palindrome(i + 1, j - 1))
        hashset = {}
        def permute(i, j):
            nonlocal hashset
            if (i,j) in hashset:
                return hashset[(i,j)]

            if (s[i] == s[j]):
                if j - i <= 2 or permute(i + 1, j - 1):
                    hashset[(i,j)] = True 
                    return True 
            
            hashset[(i,j)] = False
            return False

        max_length = 0
        start_index = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if (j - i + 1 > max_length and permute(i,j)):
                    max_length = j - i + 1
                    start_index = i 
        return s[start_index: start_index + max_length]
                

                
