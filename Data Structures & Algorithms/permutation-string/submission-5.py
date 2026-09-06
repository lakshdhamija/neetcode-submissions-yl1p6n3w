class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        countS1, countS2, l, r = [0] * 26, [0] * 26, 0, 0
        for c in s1: countS1[ord(c) - ord('a')] += 1
        while r < len(s2):
            countS2[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                countS2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if tuple(countS1) == tuple(countS2): return True
            r += 1
        return False
            
