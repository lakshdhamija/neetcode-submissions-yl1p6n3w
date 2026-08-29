class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t): return ''
        countT, window = {}, {}
        for c in t: countT[c] = countT.get(c, 0) + 1
        have, need, l, res, resLen = 0, len(countT), 0, [-1, -1], float('inf')
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
                while have == need: # we've a match
                    if r - l + 1 < resLen:
                        res = [l, r]
                        resLen = r - l + 1
                    # print(window, l ,s[l], have, need)
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]: have -= 1
                    l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ''