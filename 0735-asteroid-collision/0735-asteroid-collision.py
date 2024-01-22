class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst_pos = []
        lst_g = []
        for i in asteroids:
            if i > 0:
                lst_pos.append(i)
            else:
                if len(lst_pos) == 0:
                    lst_g.append(i)
                else:
                    while True:
                        tmp = lst_pos[-1]
                        if tmp + i < 0:
                            lst_pos.pop()
                            if len(lst_pos) == 0:
                                lst_g.append(i)
                                break
                        elif tmp + i == 0:
                            lst_pos.pop()
                            break
                        else:
                            break
        lst_g += lst_pos
        return lst_g
        