class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        one, two = 1, 2
        for i in range(3, n + 1):
            three = one + two
            one, two = two, three
        return two