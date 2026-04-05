class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums: numSet.add(num)
        possibleStarts = []
        for num in nums:
            if (num - 1) not in numSet: possibleStarts.append(num)
        maxLength = 0
        for num in possibleStarts:
            curLength = 1
            curNum = num
            while curNum + 1 in numSet:
                curLength += 1
                curNum += 1
            maxLength = max(curLength, maxLength)
        return maxLength