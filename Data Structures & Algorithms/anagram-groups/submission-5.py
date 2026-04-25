class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for character in string:
                arr[ord('z')-ord(character)]+=1 
            hashmap[tuple(arr)].append(string)
        return list(hashmap.values())