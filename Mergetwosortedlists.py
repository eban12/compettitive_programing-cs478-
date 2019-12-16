# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode(0)
        last = merged
        c1 = l1
        c2 = l2
        while c1 and c2:
            if c1.val < c2.val:
                last.next = c1
                c1 = c1.next
            else:
                last.next = c2
                c2 = c2.next
            last = last.next

        while c1:
            last.next = c1
            c1 = c1.next
            last = last.next

        while c2:
            last.next = c2
            c2 = c2.next
            last = last.next

        return merged.next
