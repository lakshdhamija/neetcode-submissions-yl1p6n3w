class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        l, r, maxF, res = 0, 0, 0, 0
        while r < len(s):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            maxF = max(maxF, freqMap[s[r]])
            while (r - l + 1) - maxF > k:
                freqMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res 