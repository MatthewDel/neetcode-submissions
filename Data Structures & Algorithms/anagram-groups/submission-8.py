class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groupings = defaultdict(list)

        for word in strs:
            hashMap = [0] * 26
            for char in word:
                hashMap[ord(char) - ord('z')] += 1
            anagram_groupings[tuple(hashMap)].append(word)
        
        sol = []
        for key in anagram_groupings:
            sol.append(anagram_groupings[key])
        
        return sol
