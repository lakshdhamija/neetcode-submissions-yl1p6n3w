class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st, output = [], [0] * len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                poppedIdx = st.pop()
                output[poppedIdx] = i - poppedIdx
            st.append(i)
        return output