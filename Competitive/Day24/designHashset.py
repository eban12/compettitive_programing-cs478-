class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.storage = []
        for i in range(1000):
            self.storage.append(ListNode(None))

    def add(self, key: int) -> None:
        exists, idx = self._hash(key)
        if not exists:
            idx.next = ListNode(key)
            
    def remove(self, key: int) -> None:
        exists, idx = self._hash(key)
        if exists:
            idx.next = idx.next.next

    def contains(self, key: int) -> bool:
        exists, idx = self._hash(key)
        if exists:
            return True
        return False
    
    def _hash(self, key):
        idx = key % (len(self.storage) - 1)
        prev = self.storage[idx]
        current = prev.next
        while current:
            if current.key == key:
                return True, prev

            current = current.next
            prev = prev.next
        return False, prev
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
