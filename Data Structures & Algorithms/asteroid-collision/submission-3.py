class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            toPush = True
            while stack and a < 0 and stack[-1] > 0: # collision
                if abs(a) > stack[-1]: stack.pop() # incoming is bigger
                elif abs(a) < stack[-1]:
                    toPush = False
                    break
                else:
                    stack.pop()
                    toPush = False
                    break
            if toPush: stack.append(a)
        return stack