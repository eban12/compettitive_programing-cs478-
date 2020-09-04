class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        
        if len(vals) < 1:
            return True
        
        if len(vals) == 2:
            return vals[0] == vals[1]
        
        i = j = len(vals)//2
        if len(vals) % 2 == 0:
            i -= 1
        
        while i >= 0 and j < len(vals):
            print(i,j)
            if vals[i] != vals[j]:
                return False
            i -= 1
            j += 1
        return True
