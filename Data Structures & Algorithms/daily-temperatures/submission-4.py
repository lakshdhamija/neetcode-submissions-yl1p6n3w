class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st, res = [], [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                poppedIdx = st.pop()
                res[poppedIdx] = i - poppedIdx
            st.append(i)
        return res