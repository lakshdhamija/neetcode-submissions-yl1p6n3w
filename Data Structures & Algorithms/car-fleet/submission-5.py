class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedPos, st = [], []
        for i in range(len(position)): speedPos.append((position[i], speed[i]))
        speedPos.sort(reverse=True)
        # print(speedPos)
        for i in range(len(speedPos)):
            pos, sp = speedPos[i]
            timeToDest = (target - pos)/sp
            # print(timeToDest, st)
            if st and st[-1] >= timeToDest: continue # new car was trying to reach before prevCar but got limited
            st.append(timeToDest)
        return len(st)