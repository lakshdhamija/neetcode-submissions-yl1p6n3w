class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix, postfix = [1] * len(nums), [1] * len(nums)
        # for i in range(1, len(nums)): prefix[i] = prefix[i - 1] * nums[i - 1]
        # for i in range(len(nums) - 2, -1, -1): postfix[i] = postfix[i + 1] * nums[i + 1]
        # output = []
        # for i in range(len(nums)): output.append(prefix[i] * postfix[i])
        # return output
        res = [1] * len(nums)
        for i in range(1, len(nums)): res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= postfix * nums[i + 1]
            postfix *= nums[i + 1]
        return res
            

