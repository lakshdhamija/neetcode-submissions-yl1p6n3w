class Solution:
    def decodeString(self, s: str) -> str:
        strSt, countSt, cur, k = [], [], "", 0
        for c in s:
            # print(strSt, countSt, cur, k)
            if c.isdigit(): k = k * 10 + int(c)
            elif c.isalpha(): cur += c
            elif c == '[':
                strSt.append(cur)
                countSt.append(k)
                cur, k = "", 0
            elif c == ']':
                temp = cur
                poppedCur, count = strSt.pop(), countSt.pop()
                # print("<<", poppedCur, count)
                poppedCur += temp * count
                cur = poppedCur
        return cur