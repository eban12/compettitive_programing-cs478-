class MyStack:

    def __init__(self):
        self.values = []
        self.copy = []
        
    def push(self, x: int) -> None:
        self.values.append(x)

    def pop(self) -> int:
        while len(self.values) > 1:
            self.copy.append(self.values.pop(0))
        
        temp = self.values.pop(0)
        self.values, self.copy = self.copy, self.values
        return temp        

    def top(self) -> int:
        while len(self.values) > 1:
            self.copy.append(self.values.pop(0))
        
        temp = self.values.pop(0)
        self.values, self.copy = self.copy, self.values
        self.values.append(temp)
        return temp
        

    def empty(self) -> bool:
        return self.values == []