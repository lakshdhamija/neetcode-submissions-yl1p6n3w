class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [0] * len(nums)
        # prefix[0] = 1
        # for i in range(1, len(nums)): prefix[i] = prefix[i - 1] * num
        # print(prefix)
        zeros, pro = 0, 1
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            pro *= num
        if zeros > 1: return [0] * len(nums)
        res = []
        for i in range(len(nums)):
            if zeros == 1: 
                if nums[i] == 0: res.append(pro)
                else: res.append(0)
            else:
                res.append(pro // nums[i])
        return res
