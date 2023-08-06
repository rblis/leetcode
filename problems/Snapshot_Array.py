class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[0,0]] for _ in range(length)]
        self.snaps = 0        

    def set(self, index: int, val: int) -> None:
        if (self.arr[index] and self.arr[index][-1][1] == self.snaps):
            self.arr[index][-1] = [val, self.snaps]
        else:
            self.arr[index].append([val, self.snaps])

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        nums = self.arr[index]
        lo,hi = 0, len(nums)-1
        ans = -1 
        while lo <= hi:
            mid = lo + hi >> 1
            if nums[mid][1] > snap_id:
                hi = mid - 1
            elif nums[mid][1] <= snap_id:
                ans = mid
                lo = mid + 1
        if ans == -1: return 0
        return nums[ans][0]


# Your SnapshotArray object will be instantiated and called as such:
ques = ["SnapshotArray","set","snap","snap","set","set","get","get","get"]
vals = [[3],[1,6],[],[],[1,19],[0,4],[2,1],[2,0],[0,1]]
obj = None
for i in range(len(ques)):
    if ques[i] == "SnapshotArray":
        obj = SnapshotArray(vals[i][0])
    elif ques[i] == "set":
        obj.set(vals[i][0],vals[i][1])
    elif ques[i] == "snap":
        print(obj.snap())
    else:
        print(obj.get(vals[i][0], vals[i][1]))