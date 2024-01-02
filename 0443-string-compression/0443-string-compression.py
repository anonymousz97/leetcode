class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("?")
        cnt = 1
        s = ""
        c_pos = chars[0]
        for i in range(1, len(chars)):
            if chars[i] == c_pos:
                cnt += 1
            else:
                if cnt == 1:
                    s += c_pos
                else:
                    s += c_pos
                    s += str(cnt)
                    cnt = 1
                c_pos = chars[i]
        for item in s[::-1]:
            chars.insert(0,item)
        return len(s)