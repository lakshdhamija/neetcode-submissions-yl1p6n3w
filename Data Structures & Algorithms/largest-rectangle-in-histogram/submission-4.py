class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, res = [], 0
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                poppedIdx, poppedHeight = st.pop()
                start = poppedIdx
                res = max(res, (i - poppedIdx) * poppedHeight)
            st.append((start, h))
        for i, h in st: res = max(res, (len(heights) - i) * h)
        return res