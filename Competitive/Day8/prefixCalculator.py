class Stack:
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)

    def pop(self):
        if len(self.values) > 0:
            return self.values.pop()


def preFixCalculator(lst):
    opr = ['+', '-', '*', '/']
    operands = Stack()
    lst = lst[::-1]
    for i in lst:
        if i not in opr:
            operands.insert(i)
        else:
            temp1 = operands.pop()
            temp2 = operands.pop()
            s = eval(temp1 + ' ' + i + ' ' + temp2)
            operands.insert(str(s))
    return operands.pop()