class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        value_set = set()
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            value_at_right = s[right]
            if value_at_right in value_set:
                while value_at_right in value_set:
                    value_set.remove(s[left])
                    left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
            value_set.add(value_at_right)
        
        
        return max_length
            
