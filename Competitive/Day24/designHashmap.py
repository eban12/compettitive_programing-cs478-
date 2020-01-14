class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.storage = []
        for i in range(1000):
            self.storage.append(ListNode(None, None))

    def put(self, key: int, value: int) -> None:
        exists, idx = self._hash(key)
        if exists:
            idx.next.val = value
        else:
            idx.next = ListNode(key, value)

    def get(self, key: int) -> int:
        exists, idx = self._hash(key)
        if exists:
            return idx.next.val
        return -1

    def remove(self, key: int) -> None:
        exists, idx = self._hash(key)
        if exists:
            idx.next = idx.next.next

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
