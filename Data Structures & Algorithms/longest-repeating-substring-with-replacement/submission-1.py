class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount, res, l, maxF = {}, 0, 0, 0
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            maxF = max(maxF, charCount[s[r]])
            if (r - l + 1) - maxF > k:
                charCount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res