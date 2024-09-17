class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queueVisit = []
        lstVisit = {i:0 for i in range(len(rooms))}
        lstVisit[0] = 1
        queueVisit += rooms[0]
        while len(queueVisit) > 0:
            nextVisit = queueVisit.pop(0)
            queueVisit += rooms[nextVisit]
            rooms[nextVisit] = []
            lstVisit[nextVisit] = 1
            if 0 not in lstVisit.values():
                return True
        if 0 not in lstVisit.values():
            return True
        return False
        