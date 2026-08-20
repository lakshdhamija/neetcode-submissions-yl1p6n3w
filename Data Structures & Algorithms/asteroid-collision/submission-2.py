class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0: stack.append(ast)
            else:
                toPush = False
                if not stack or stack[-1] < 0: toPush = True
                while stack and not (stack[-1] < 0) and stack[-1] <= abs(ast):
                    ele = stack.pop()
                    if ele == abs(ast): break
                    if not stack or stack[-1] < 0: toPush = True
                if toPush: stack.append(ast)
        return stack
