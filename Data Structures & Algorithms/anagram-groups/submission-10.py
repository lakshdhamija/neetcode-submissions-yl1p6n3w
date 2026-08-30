class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for st in strs:
            sortedStr = "".join(sorted(st))
            if sortedStr in strMap: strMap[sortedStr].append(st)
            else: strMap[sortedStr] = [st]
        return list(strMap.values())