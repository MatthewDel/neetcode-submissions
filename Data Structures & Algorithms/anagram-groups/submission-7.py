class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('z')] += 1
            tupFreq = tuple(freq)
            hashMap[tupFreq].append(word)
        sol = []
        for arr in hashMap.values():
            sol.append(arr)
        return sol 
            