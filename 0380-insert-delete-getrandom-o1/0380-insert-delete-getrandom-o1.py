import random
class RandomizedSet:

    def __init__(self):
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.list:
            self.list.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.list:
            return False
        self.list.remove(val)
        return True

    def getRandom(self) -> int:
        r = random.sample(self.list,1)[0]
        return r


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()