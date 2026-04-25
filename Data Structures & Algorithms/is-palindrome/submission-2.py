class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_string = ""
        s=s.lower()
        alpha = set('abcdefghijklmnopqrstuvwxyz0123456789')
        for c in range(len(s)-1, -1, -1):
            if s[c] in alpha:
                final_string += s[c]
 
        return final_string == final_string[::-1]
            