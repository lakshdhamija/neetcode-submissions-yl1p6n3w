class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        one = two = three = False
        for x, y, z in triplets:
            if x > a or y > b or z > c: continue
            one = one or x == a
            two = two or y == b
            three = three or z == c
        return one and two and three