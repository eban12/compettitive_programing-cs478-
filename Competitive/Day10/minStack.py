class MinStack:

    def __init__(self):
        self.items = []
        self.min = None
        
    def push(self, x: int) -> None:
        self.items.append(x)
        if self.min == None:
            self.min = x
        elif self.min > x:
            self.min = x

    def pop(self) -> None:
        temp = self.items.pop()
        if temp == self.min:
            self.min = min(self.items)
        return temp

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min