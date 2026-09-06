class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        res, resLen, l, r, countS, countT = [-1, -1], float('inf'), 0, 0, {}, {}
        for c in t: countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        while r < len(s):
            countS[s[r]] = countS.get(s[r], 0) + 1
            # print(countS, countT, s[r] in countT, countS[s[r]])
            if s[r] in countT and countS[s[r]] == countT[s[r]]: have += 1
            # print("<< need", have)
            while have == need: # valid string
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]: have -= 1
                l += 1
            r += 1
        print(res)
        return s[res[0]:res[1]+1] if res[0] != -1 else ''