class MinStack:

    def __init__(self):
        self.st, self.minSt = [], []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minSt and self.minSt[-1] < val: self.minSt.append(self.minSt[-1])
        else: self.minSt.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
