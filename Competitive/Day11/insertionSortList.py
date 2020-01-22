# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        sorted = ListNode(head.val)
        head = head.next
        while head:
            t = head.val
            
            if sorted.val > t:
                temp = ListNode(t)
                temp.next = sorted
                sorted = temp
            else:
                current = sorted
                prev = sorted
                while current and current.val <= t:
                    prev = current
                    current = current.next
                temp = ListNode(t)
                prev.next = temp
                temp.next = current
            head = head.next
        return sorted
                    
