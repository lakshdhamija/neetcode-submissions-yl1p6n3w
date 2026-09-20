class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, l, r, q = [], 0, 0, deque()
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: q.pop()
            q.append(r)
            if q[0] < r - k + 1: q.popleft()
            if r >= k - 1: res.append(nums[q[0]])
            r += 1
        return res