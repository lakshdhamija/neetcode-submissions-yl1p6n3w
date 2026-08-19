class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output, q = [], collections.deque()
        l = r = 0
        while r < len(nums):
            while q and q[-1] < nums[r]: q.pop()
            q.append(nums[r])
            if r - l + 1 > k:
                if nums[l] == q[0]: q.popleft()
                l += 1
            if r - l + 1 == k: output.append(q[0])
            r += 1
        return output
                