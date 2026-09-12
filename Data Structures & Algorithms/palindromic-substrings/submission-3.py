class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = i, i 
            while l >= 0 and r < len(s):
                # print("entered1", l, r)
                if s[l] == s[r]:
                    # print("added1", l, r)
                    res += 1
                else: break
                l, r = l - 1, r + 1
            l, r = i, i + 1
            # print("before enterd2", l, r, l >= 0, r < len(s))
            while l >= 0 and r < len(s):
                # print("entered2", l, r)
                if s[l] == s[r]:
                    # print("added2", l, r)
                    res += 1
                else: break
                l, r = l - 1, r + 1
        return res