class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 

        while left < right:
            if s[left] != s[right]:
                return self.is_Palindrome(left + 1, right, s) or self.is_Palindrome(left, right - 1, s)
            left += 1
            right -= 1
        return True 

    def is_Palindrome(self, left, right, arr) -> bool:
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True 
    
    