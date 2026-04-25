class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        arr_s = [0] * 26 
        arr_t = [0] * 26

        for i in range(len(s)):
            arr_s[ord('z') - ord(s[i])] += 1
            arr_t[ord('z') - ord(t[i])] += 1

        return arr_s == arr_t

        