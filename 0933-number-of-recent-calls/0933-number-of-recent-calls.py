class RecentCounter:

    def __init__(self):
        self.list = []
        

    def ping(self, t: int) -> int:
        self.list.append(t)
        pos = []
        for idx, i in enumerate(self.list):
            if t - i  <= 3000:
                self.list = self.list[idx:]
                break
        return len(self.list)
                


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)