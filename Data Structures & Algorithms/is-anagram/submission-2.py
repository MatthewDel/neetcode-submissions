class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = {}
        for char in s:
            if char not in hashset:
                hashset[char] = 1
            else:
                hashset[char] += 1
        
        for char in t:
            if char not in hashset or hashset[char]==0:
                return False
            else:
                hashset[char] -= 1

        for key in hashset:
            if hashset[key] != 0:
                return False
        return True 