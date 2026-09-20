class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        res, resLen, l, r, countT, countS = [-1, -1], float('inf'), 0, 0, {}, {}
        for c in t: countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        while r < len(s):
            countS[s[r]] = countS.get(s[r], 0) + 1
            if s[r] in countT and countT[s[r]] == countS[s[r]]: have += 1
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                countS[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > countS[s[l]]: have -= 1
                l += 1
            r += 1
        return s[res[0] : res[1] + 1] if res[0] != -1 else ''
                    
                    