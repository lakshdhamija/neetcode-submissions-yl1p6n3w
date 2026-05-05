class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for st in strs:
            ctMap = [0] * 26
            for c in st: ctMap[ord(c) - ord('a')] += 1
            if tuple(ctMap) in strMap: strMap[tuple(ctMap)].append(st)
            else: strMap[tuple(ctMap)] = [st]
        return list(strMap.values())
