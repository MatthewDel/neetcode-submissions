class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            hashmap[''.join(sorted(strs[i]))].append(strs[i])
        sol = []
        for key in hashmap:
            sol.append(hashmap[key])

        return sol