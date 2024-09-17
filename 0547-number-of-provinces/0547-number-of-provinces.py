class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        lstVisit = [0] * len(isConnected)
        cnt = 0
        c_node = 0
        while 0 in lstVisit:
            lstVisit[c_node] = 1
            queueVisit = []
            queueVisit += [idx for idx, i in enumerate(isConnected[c_node]) if i == 1 and idx != c_node]
            while queueVisit:
                k = queueVisit.pop()
                if not lstVisit[k]:
                    queueVisit += [idx for idx, i in enumerate(isConnected[k]) if i == 1 and idx != k]
                    lstVisit[k] = 1
            cnt += 1
            for idx, i in enumerate(lstVisit):
                if i == 0:
                    # print("assign next node")
                    c_node = idx
        return cnt
                
                
        