class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alpha  = set('abcdefghijklmnopqrstuvwxyz0123456789')
        i = 0 
        j = len(s)-1
        while i<j:
            while i<j and s[i] not in alpha:
                i += 1
            while i<j and s[j] not in alpha:
                j -=1 
            if s[i] != s[j]:
                return False
            i += 1 
            j -= 1
        return True