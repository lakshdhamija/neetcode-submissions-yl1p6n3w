class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea, st = 0, []
        for i, h in enumerate(heights):
            start = i
            while st and st[-1][1] > h:
                poppedIdx, height = st.pop()
                area = (i - poppedIdx) * height
                maxArea = max(maxArea, area)
                start = poppedIdx
            st.append((start, h))
        for i, h in st: maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
