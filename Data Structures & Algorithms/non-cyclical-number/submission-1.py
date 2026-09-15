class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set([n])
        while n != 1:
            currN, n = n, 0
            while currN != 0:
                digit = currN % 10
                currN //= 10
                n += digit ** 2
            if n in hashset: return False
            hashset.add(n)
        return True
    