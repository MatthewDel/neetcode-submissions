class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        arr_s = [0] * 26 

        for i in range(len(s)):
            arr_s[ord('z') - ord(s[i])] += 1
            arr_s[ord('z') - ord(t[i])] -= 1

        for num in arr_s:
            if num !=0:
                return False
        
        return True

        