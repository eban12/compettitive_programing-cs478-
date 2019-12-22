class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val
        

    def addAtHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        if self.tail is None:
            self.tail = self.head
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        if self.tail is None:
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
            self.size += 1
        if self.head is None:
            self.head = self.tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            temp = current.next
            current.next = Node(val)
            current.next.next = temp
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            if index + 1 == self.size:
                self.tail = current
        self.size -= 1