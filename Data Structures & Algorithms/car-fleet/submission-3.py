class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carArr = []
        for i in range(len(position)): carArr.append((position[i], speed[i]))
        carArr.sort(reverse=True)
        print(carArr)
        st = []
        for pos, sp in carArr:
            reachTime = (target - pos) / sp
            if st and st[-1] >= reachTime: continue
            st.append(reachTime)
        return len(st)
