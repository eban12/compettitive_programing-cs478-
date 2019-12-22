def reverseList(head: ListNode) -> ListNode:
        if head == None:
            return head
        current = head.next
        res = ListNode(head.val)
        while current:
            temp = ListNode(current.val)
            temp.next = res
            res = temp
            current = current.next
        return res