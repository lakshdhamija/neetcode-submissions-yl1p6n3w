class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = -1, 0
        for i in range(len(s)):
            l, r = i, i # odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l, r = l - 1, r + 1
            l, r = i, i + 1 # even length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIdx = l
                l, r = l - 1, r + 1
        return s[resIdx: resIdx + resLen] if resLen != -1 else ''