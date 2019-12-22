class MyQueue:

    def __init__(self):
        self.values = []
        self.copy = []
        

    def push(self, x: int) -> None:
        self.values.append(x)
        

    def pop(self) -> int:
        while len(self.values) > 1:
            self.copy.append(self.values.pop())
        
        temp = self.values.pop()
        while self.copy != []:
            self.values.append(self.copy.pop())
        return temp

    def peek(self) -> int:
        while len(self.values) > 1:
            self.copy.append(self.values.pop())
        
        temp = self.values.pop()
        self.values.append(temp)
        while self.copy != []:
            self.values.append(self.copy.pop())
        return temp
        
    def empty(self) -> bool:
        return self.values == []