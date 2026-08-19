class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars, l, r, res = set(), 0, 0, 0
        while l < len(s) and r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            r += 1
            res = max(res, len(chars))
        return res