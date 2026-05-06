class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        l, r, charSet, res = 0, 1, set(s[0]), 0
        while l < len(s) and r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            r += 1
            res = max(res, len(charSet))
        return res
        