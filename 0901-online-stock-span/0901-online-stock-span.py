class StockSpanner:

    def __init__(self):
        self.lst = []
        self.val = []

    def next(self, price: int) -> int:
        if len(self.lst) == 0:
            self.lst.append(price)
            self.val.append(1)
            return 1
        self.lst.append(price)
        if self.lst[-1] < self.lst[-2]:
            self.val.append(1)
            return 1
        else:
            # print(self.lst, self.val)
            cnt = 1
            ix = len(self.lst) - 1
            while True:
                # print(ix, self.val[ix-1], self.val[0])
                n_pos = ix-self.val[ix-1]
                cnt += self.val[ix-1]
                if n_pos == 0:
                    self.val.append(cnt)
                    return cnt
                if price < self.lst[n_pos-1]:
                    self.val.append(cnt)
                    return cnt
                else:
                    ix = n_pos
                if ix == 0:
                    self.val.append(cnt)
                    return cnt
                


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)