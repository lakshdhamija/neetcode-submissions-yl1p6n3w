class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, maxArea = [], 0
        for i, h in enumerate(heights):
            start = i
            while st and h < st[-1][1]:
                poppedIdx, poppedH = st.pop()
                width = i - poppedIdx
                start = poppedIdx
                maxArea = max(maxArea, width * poppedH)
            st.append((start, h))
        for i, h in st: maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea
