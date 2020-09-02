# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        tail = head
        while n > 0:
            tail = tail.next
            n-=1
        
        while tail and tail.next:
            current = current.next
            tail = tail.next
        
        if not tail:
            head = head.next
        else:
            current.next = current.next.next
        
        return head
