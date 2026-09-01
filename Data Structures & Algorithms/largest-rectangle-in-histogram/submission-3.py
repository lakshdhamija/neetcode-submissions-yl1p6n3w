class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea, st = 0, []
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                poppedIndex, poppedHeight = st.pop()
                start = poppedIndex
                maxArea = max(maxArea, (i - poppedIndex) * poppedHeight)
            st.append((start, h))
        for i, h in st: maxArea = max((len(heights) - i) * h, maxArea)
        return maxArea