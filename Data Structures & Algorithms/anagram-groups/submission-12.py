class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charsMap = {}
        for st in strs:
            count = [0] * 26
            for c in st: count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in charsMap: charsMap[key].append(st)
            else: charsMap[key] = [st]
        return list(charsMap.values())