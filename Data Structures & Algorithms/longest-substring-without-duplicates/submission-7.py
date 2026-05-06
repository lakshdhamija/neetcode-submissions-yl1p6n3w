class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        l, r, seen, res = 0, 1, {}, 0
        seen[s[l]] = l
        while l < len(s) and r < len(s):
            if s[r] in seen and seen[s[r]] >= l: l = seen[s[r]] + 1
            seen[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res
