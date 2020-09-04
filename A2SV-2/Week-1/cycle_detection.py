def has_cycle(head):
    slow = head
    fast = head
    i = 0
    while i < 4 and fast:
        fast = fast.next
        i += 1
    
    while fast and fast.next:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False
