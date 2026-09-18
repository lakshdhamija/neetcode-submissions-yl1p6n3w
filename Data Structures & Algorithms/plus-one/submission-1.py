class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        res, carry, i = digits[::-1], 1, 0
        while carry and i < len(res):
            if res[i] == 9: res[i] = 0
            else:
                res[i] += 1
                carry = 0
            i += 1
        if carry: res.append(1)
        return res[::-1]


