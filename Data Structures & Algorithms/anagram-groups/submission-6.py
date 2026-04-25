class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            temp_set = [0] * 26
            for char in string:
                temp_set[ord(char) - ord('a')] += 1
            hashmap[tuple(temp_set)].append(string)
        
        sol = []
        for key in hashmap:
            sol.append(hashmap[key])

        return sol 