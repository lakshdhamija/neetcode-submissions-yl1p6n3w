class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for st in strs:
            cMap = [0] * 26
            for c in st: cMap[ord(c) - ord('a')] += 1
            if tuple(cMap) in strMap: strMap[tuple(cMap)].append(st)
            else: strMap[(tuple(cMap))] = [st]
        return list(strMap.values())