# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head: ListNode) -> ListNode:
    current = head
    while current:
        temp = current
        while current.next and temp.val == current.next.val:
            temp.next = current.next.next if current.next.next else None
        current = current.next
    return head