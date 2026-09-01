class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st, maxArea = [], 0
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > heights[i]:
                poppedIdx, poppedHeight = st.pop()
                maxArea = max(maxArea, (i - poppedIdx) * poppedHeight)
                start = poppedIdx
            st.append((start, h))
        for i, h in st: maxArea = max(h * (len(heights) - i), maxArea)
        return maxArea
