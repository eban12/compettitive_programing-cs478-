# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        # res = lists[0]
        n = len(lists)
        j = 1
        while j < n:
            for i in range(0,n - j, j * 2):
                lists[i] = self.merge(lists[i], lists[i + j])
            j *= 2
        return lists[0]
        
    
    def merge(self, head1, head2):
        dh = ListNode(0)
        current = dh
        while head1 and head2:
            if head1.val <= head2.val:
                t = ListNode(head1.val)
                current.next = t
                current = t
                head1 = head1.next
            else:
                t = ListNode(head2.val)
                current.next = t
                current = t
                head2 = head2.next
        
        if head1:
            current.next = head1
        
        if head2:
            current.next = head2
        
        return dh.next
    
