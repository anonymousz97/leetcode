class Solution:
    def process(self, x):
        n = len(x) - 1
        cnt = 1
        res = []
        while True:
            if n == 0:
                break
            if x[n] == x[n-1]:
                cnt += 1
            else:
                res.append(str(cnt) + x[n])
                cnt = 1
            n -= 1
        if cnt == 1:
            res.append("1"+ x[0])
        else:
            res.append(str(cnt) + x[n])
        return "".join(res[::-1])

            


    def countAndSay(self, n: int) -> str:
        c = "1"
        for i in range(2, n+1, 1):
            c = self.process(c)
        return c
        