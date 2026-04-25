class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set_one = {}
        hash_set_two = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hash_set_one[s[i]] = 1 + hash_set_one.get(s[i], 0)
            hash_set_two[t[i]] = 1 + hash_set_two.get(t[i], 0)
        
        return hash_set_one == hash_set_two