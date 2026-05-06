class MinStack:

    def __init__(self):
        self.minVal = 0
        self.st = []

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(0)
            self.minVal = val
        else:
            self.st.append(val - self.minVal)
            if val - self.minVal < 0: self.minVal = val

    def pop(self) -> None:
        poppedVal = self.st.pop()
        if poppedVal < 0: self.minVal -= poppedVal      

    def top(self) -> int:
        if self.st[-1] < 0: return self.minVal
        else: return self.st[-1] + self.minVal

    def getMin(self) -> int:
        return self.minVal
