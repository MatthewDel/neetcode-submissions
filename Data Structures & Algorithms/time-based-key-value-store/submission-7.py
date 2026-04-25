class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))
        return 

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        left = 0
        right = len(self.hashmap[key])-1 
        while left<=right:
            mid = (left + right) // 2 
            if self.hashmap[key][mid][1] ==  timestamp:
                return self.hashmap[key][mid][0]
            elif self.hashmap[key][mid][1] < timestamp:
                left = mid + 1
                res = self.hashmap[key][mid][0]
            else:
                right = mid - 1
        
        return res
