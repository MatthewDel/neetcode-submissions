class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set('abcdefghijklmnopqrstuvwxyz0123456789')
        s = s.lower()
        initial = 0
        end = len(s)-1 
        while initial<end:
            while s[initial] not in alphanumeric and initial<end:
                initial+=1
            while s[end] not in alphanumeric and initial<end:
                end-=1
            if initial<end and (s[end]) != (s[initial]):
                return False
            initial += 1
            end -= 1
        return True 