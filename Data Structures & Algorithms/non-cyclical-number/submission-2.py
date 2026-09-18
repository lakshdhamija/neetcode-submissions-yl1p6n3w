class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set([n])
        while n != 1:
            curN, n = n, 0
            while curN != 0:
                digit = curN % 10
                curN //= 10
                n += digit ** 2
            if n in hashset: return False
            hashset.add(n)
        return True