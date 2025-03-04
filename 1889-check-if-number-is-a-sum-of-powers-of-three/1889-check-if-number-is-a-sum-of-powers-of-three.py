class Solution:
    def __init__(self):
        self.lst = []
        state = [0 for x in range(15)]
        while True:
            for i in range(len(state) - 1, -1, -1):
                if state[i] == 0:
                    state[i] = 1
                    for j in range(i+1, len(state), 1):
                        state[j] = 0
                    break
            num = 0
            for i in range(len(state)):
                num += 3 ** (len(state) - 1 - i) * state[i]
            self.lst.append(num)
            if sum(state) == len(state):
                break
            # if len(self.lst) == 10000:
            #     break

    def checkPowersOfThree(self, n: int) -> bool:
        if n in self.lst:
            return True
        return False
        