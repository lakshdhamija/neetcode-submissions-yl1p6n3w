class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        hand.sort()
        numCounts = {}
        for num in hand: numCounts[num] = numCounts.get(num, 0) + 1
        for num in hand:
            cnt = numCounts[num]
            if cnt:
                for i in range(num, num + groupSize):
                    if i not in numCounts or numCounts[i] < cnt: return False
                    numCounts[i] -= cnt
        return True
        
