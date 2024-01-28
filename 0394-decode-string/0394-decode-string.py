class Solution(object):
    def decodeString(self, s):
        stack = []
        for i in s:
            print(i, stack)
            if i == "]":
                tmp = ""
                while stack[-1] != '[':
                    out = stack.pop()
                    tmp += out
                stack.pop()
                times = ""
                while stack and stack[-1].isdigit():
                    out = stack.pop()
                    times += out
                times = int(times[::-1])
                stack.extend(list(tmp[::-1])*times)
                # print(times, tmp[::-1])
            else:
                stack.append(i)
        print(stack)
        return "".join(x for x in stack)