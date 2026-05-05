class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = [0] * 26, [0] * 26
        for c in s: sMap[ord(c) - ord('a')] += 1
        for c in t: tMap[ord(c) - ord('a')] += 1
        return sMap == tMap