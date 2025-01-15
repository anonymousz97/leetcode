class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a = [x for x in str(bin(num1)[2:])]
        b = [x for x in str(bin(num2)[2:])]
        a = ['0'] * (max(len(a), len(b)) - len(a)) + a
        b = ['0'] * (max(len(a), len(b)) - len(b)) + b
        n1 = a.count("1")
        n2 = b.count("1")
        if n1 == n2:
            return num1
        if n1 > n2:
            tmp = n2
            num = ""
            for idx, i in enumerate(a):
                if i == '1':
                    tmp -= 1
                    if tmp == 0:
                        num += a[idx]
                        num += "0" * (len(a)-len(num))
                        break
                num += a[idx]
            return int(''.join(num), 2)
        else:
            tmp = n2 - n1
            num = a[::-1]
            for idx, i in enumerate(num):
                if i == '0':
                    num[idx] = '1'
                    tmp -= 1
                    if tmp == 0:
                        break
            return int(''.join(num[::-1]), 2)

                




        