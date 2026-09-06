class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter, l, r, res, maxF = {}, 0, 0, 0, 0
        while r < len(s):
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxF = max(maxF, counter[s[r]])
            while (r - l + 1) - maxF > k: # invalid so start reducing from front
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
