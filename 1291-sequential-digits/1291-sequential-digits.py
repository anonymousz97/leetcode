class Solution:
    def __init__(self):
        self.list_num = []
        for i in range(2,10):
            tmp = []
            for j in range(1,11-i):
                tmp.append(int(''.join(str(x) for x in range(j,j+i))))
            self.list_num.extend(tmp)
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # s_idx = -2
        # e_idx = -2
        # s_l = -1
        # e_h = -1
        # for idx,i in self.list_num:
        #     if i[-1] > low and s_idx == -2:
        #         s_idx = idx
        #         for idx2, j in i:
        #             if j > low:
        #                 s_l = idx2
        #                 break
        #     if i[0] > high and e_idx == -2:
        #         e_idx = idx - 1
        #         if e_idx == -1:
        #             e_idx = 0
        #         for idx2, j in self.list_num[e_idx]:
        #             if j
        lst_out = []
        for i in self.list_num:
            if i >= low and i <= high:
                lst_out.append(i)
                
        return lst_out
            
            
        
        