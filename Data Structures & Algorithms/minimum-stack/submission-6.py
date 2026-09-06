class MinStack:

    def __init__(self):
        self.st = []
        self.minVal = 0

    def push(self, val: int) -> None:
        if not len(self.st):
            self.st.append(0)
            self.minVal = val
        else:
            self.st.append(val - self.minVal) # this will be negative if val < minVal
            if val < self.minVal: self.minVal = val

    def pop(self) -> None:
        poppedItem = self.st.pop() # if < 0, this is cur min val - old min val
        if poppedItem < 0: self.minVal -= poppedItem

    def top(self) -> int:
        if self.st[-1] < 0: return self.minVal
        return self.st[-1] + self.minVal

    def getMin(self) -> int:
        return self.minVal
