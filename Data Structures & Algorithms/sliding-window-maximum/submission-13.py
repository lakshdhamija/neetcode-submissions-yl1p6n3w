class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = deque(), []
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if i >= k - 1: # valid window
                if q[0] <= i - k: q.popleft()
                res.append(nums[q[0]])
        return res
