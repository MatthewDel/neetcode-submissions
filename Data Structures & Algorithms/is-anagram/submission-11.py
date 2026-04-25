class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSet = {}
        for char in s:
            if char in hashSet:
                hashSet[char] += 1
            else:
                hashSet[char] = 1

        for char in t:
            if char not in hashSet or hashSet[char] == 0:
                return False
            else:
                hashSet[char] -= 1
            
        for key in hashSet:
            if hashSet[key] != 0:
                return False

        return True
