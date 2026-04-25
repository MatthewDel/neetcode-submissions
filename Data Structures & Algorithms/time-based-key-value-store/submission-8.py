class TimeMap:

    def __init__(self):
        self.hash_set = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_set[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.hash_set[key]) - 1
        value = ""
        while left <= right:
            mid = (left + right) // 2
            if self.hash_set[key][mid][0] == timestamp:
                return self.hash_set[key][mid][1]
            elif self.hash_set[key][mid][0] < timestamp:
                left = mid + 1
                value = self.hash_set[key][mid][1]
            else:
                right = mid - 1
        return value