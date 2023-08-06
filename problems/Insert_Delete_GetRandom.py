import collections
import random


class RandomizedSet:

    def __init__(self):
        self.vals = collections.defaultdict(list) #value map to index
        self.nums = [] #contains values

    def insert(self, val: int) -> bool:
        present = True
        if val in self.vals: present = False
        self.nums.append(val)
        self.vals[val].append(len(self.nums) - 1)
        return present

    def remove(self, val: int) -> bool:
        if val not in self.vals: return False
        index = self.vals[val].pop()
        if index != len(self.nums)-1:
            swap = 0
            for i,v in enumerate(self.vals[self.nums[-1]]):
                if v == len(self.nums) -1:
                    swap = i
                    break
            self.vals[self.nums[-1]][swap] = index
            self.nums[-1], self.nums[index] = self.nums[index], self.nums[-1]
        self.nums.pop()
        if self.vals[val] == []: self.vals.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(1)
param_2 = obj.remove(2)
print(obj.getRandom())