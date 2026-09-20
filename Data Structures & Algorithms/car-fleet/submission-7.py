class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars, st = [], []
        for i in range(len(position)): cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        for pos, sp in cars:
            reachTime = (target - pos) / sp
            if st and st[-1] >= reachTime: continue
            st.append(reachTime)
        return len(st)