class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        right = 0
        hashset = set()
        while right < len(s):
            if s[right] in hashset:
                while s[left] != s[right]:
                    hashset.remove(s[left])
                    left += 1
                hashset.remove(s[left])
                left += 1
            else:
                hashset.add(s[right])
                maxLength = max(right - left + 1, maxLength)
                right += 1
        return maxLength 
                
