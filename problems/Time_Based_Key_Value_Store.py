
class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            lo,hi = 0, len(self.dic[key])-1
            while lo <= hi:
                mid = lo + hi >> 1
                if self.dic[key][mid][0] > timestamp:
                    hi = mid - 1
                elif self.dic[key][mid][0] < timestamp:
                    lo = mid + 1
                else:
                    return self.dic[key][mid][1]
        if timestamp < self.dic[key][0][0] or key not in self.dic:
            return ""
        elif timestamp > self.dic[key][-1][0]:
            return self.dic[key][-1][1]
        else:
            return self.dic[key][mid-1][1]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set('love','high',10)
obj.set('love','low',20)
print(obj.get('love',5))
print(obj.get('love',15))