class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        map1 = {}
        for ch in s:
            if ch in map1: map1[ch] += 1
            else: map1[ch] = 1
        for ch in t:
            if ch in map1: map1[ch] -= 1
        for val in map1.values():
            if val != 0: return False
        return True