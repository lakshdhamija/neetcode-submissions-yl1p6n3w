class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for st in strs:
            count = [0] * 26
            for c in st: count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in strMap: strMap[key].append(st)
            else: strMap[key] = [st]
        return list(strMap.values())