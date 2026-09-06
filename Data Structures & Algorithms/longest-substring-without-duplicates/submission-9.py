class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, charSet, res = 0, 0, set(), 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))
            r += 1
        return res