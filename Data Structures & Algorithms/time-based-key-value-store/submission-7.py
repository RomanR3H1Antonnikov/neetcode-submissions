class TimeMap:

    def __init__(self):
        self.TimeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap.setdefault(key, []).append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
        currkey_hashmap = self.TimeMap[key]
        L, R = 0, len(currkey_hashmap) - 1
        res = ""
        while L <= R:
            mid = (L + R) // 2
            if currkey_hashmap[mid][1] == timestamp:
                return currkey_hashmap[mid][0]
            elif currkey_hashmap[mid][1] < timestamp:
                L = mid + 1
                res = currkey_hashmap[mid][0]
            else:
                R = mid - 1
        return res