class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            hash_map = {}
            for i in range(len(strs)):
                arr = [0] * 26 
                for j in range(len(strs[i])):
                    arr[ord(strs[i][j])-ord('a')] += 1
                tup = tuple(arr)
                if tup in hash_map:
                    hash_map[tup].append(strs[i])
                else:
                    hash_map[tup] = [strs[i]]
            sol = []
            for key in hash_map:
                sol.append(hash_map[key])
            return sol