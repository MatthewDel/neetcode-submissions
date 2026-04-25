class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_size = 0
        index = 0
        for i in range(len(s)):
            if s[i] in char_set:
                while s[i] in char_set:
                    char_set.remove(s[index])
                    index += 1
                char_set.add(s[i])
            else:
                char_set.add(s[i])
                max_size = max(max_size, len(char_set))
        return max_size

