class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carArr, st = [], []
        for i in range(len(position)): carArr.append((position[i], speed[i]))
        carArr.sort(reverse=True)
        for pos, sp in carArr:
            reachTime = (target - pos) / sp
            if st and reachTime <= st[-1]: continue
            st.append(reachTime)
        return len(st)