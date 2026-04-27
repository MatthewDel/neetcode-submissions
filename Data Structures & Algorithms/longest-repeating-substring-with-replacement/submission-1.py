class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        max_length = 0
        left = 0
        for i in range(len(s)):
            freq[ord(s[i]) - ord('Z')] += 1

            max_freq = max(freq)
            while (i - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('Z')] -= 1
                left += 1
            max_length = max(max_length, (i - left + 1))
        return max_length