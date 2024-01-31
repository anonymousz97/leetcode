class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]
        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i] < temperatures[i+1]:
                res.append(1)
            else:
                cnt = 1
                g = int(i) + 1
                while True:
                    if temperatures[i] >= temperatures[g]:
                        if res[len(temperatures)-1-g] == 0:
                            res.append(0)
                            break
                        else:
                            cnt += res[len(temperatures)-1-g]
                            g = g + res[len(temperatures)-1-g]
                    else:
                        res.append(cnt)
                        break
            # if i == len(temperatures) - 6:
            #     print(res)
            #     break
        return res[::-1]
                        
                        
                        
                        
                        
                    
                    
                    
        