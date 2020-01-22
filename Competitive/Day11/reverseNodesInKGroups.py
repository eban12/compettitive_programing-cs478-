# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# for swap nodes in pairs just make the k = 2

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        
        start = head
        tail = None
        count = 1
        current = head
        while current:
            current = current.next
            count += 1
            if count % k == 0 and current:
                end = current
                next = end.next
                end.next = None 
                h, t = self.reverse(start)
                if start == head:
                    head = h
                else:
                    tail.next = h
                t.next = next
                start = next
                current = t
                tail = t
                
        return head
    
    def reverse(self, head):
        temp = None
        current = head
        while current:
            next = current.next
            current.next = temp
            temp = current
            current = next
        return temp, head
